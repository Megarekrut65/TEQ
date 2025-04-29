from mongoengine import DoesNotExist
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from mainapp.item_types import ITEM_TYPES, SHORT, FULL, SINGLE, MULTIPLE, SCRIPT, SCRIPT_UNITTEST
from mainapp.models.test import Test, TestDocument, ChoiceItem, Choice, TextItem, ScriptItem, ScriptUnitTestItem, \
    UnitTest
from mainapp.unit_types import UNIT_TYPES
from userapp.serializers import UserProfileSerializer
from utility.case_serializers import CamelCaseSerializer, CamelCaseModelSerializer


class ChoiceSerializer(CamelCaseSerializer):
    text = serializers.CharField(max_length=200, allow_blank=True)
    is_correct = serializers.BooleanField(default=False)

class UnitTestSerializer(CamelCaseSerializer):
    name = serializers.CharField(required=True, max_length=200)
    in_test = serializers.CharField(required=True, max_length=500)
    out_test = serializers.CharField(required=True, max_length=200)
    type = serializers.ChoiceField(choices=UNIT_TYPES, required=True)

class BaseItemSerializer(CamelCaseSerializer):
    text = serializers.CharField(max_length=500, allow_blank=True)
    type = serializers.ChoiceField(choices=ITEM_TYPES)
    grade = serializers.FloatField(min_value=0.0)
    allow_proportion = serializers.BooleanField(default=False)

    #For choice item
    choices = ChoiceSerializer(many=True, required=False)

    #For text and script item
    min_similar_percent = serializers.FloatField(required=False, min_value=0, max_value=100)
    correct_answer = serializers.CharField(max_length=5000, required=False, allow_blank=True, allow_null=True)

    language = serializers.CharField(max_length=50, required=False, allow_blank=True, allow_null=True)

    #For unittest script item
    public_unittests = UnitTestSerializer(many=True, required=False)
    private_unittests = UnitTestSerializer(many=True, required=False)

    def validate(self, data):
        question_type = data.get("type")
        language = data.get("language", None)
        choices = data.get("choices", [])
        public_unittests = data.get("public_unittests", [])
        private_unittests = data.get("private_unittests", [])

        if question_type in [SHORT, FULL, SCRIPT]:
            return data

        if question_type in [SCRIPT_UNITTEST]:
            if len(public_unittests) < 1 and len(private_unittests) < 1:
                raise ValidationError("At least one unit test is required for public and private group")
            if not language:
                raise ValidationError("Language is required for unittest item")

            return data


        if len(choices) < 1:
            raise ValidationError("At least one choices are required.")

        if question_type == SINGLE:
            correct = len([choice for choice in choices if choice["is_correct"]])
            if correct < 0:
                raise ValidationError("Exactly one choice must be marked as correct.")

        return data

    def _get_choices(self, choices):
        return [Choice(**choice) for choice in choices]

    def _get_unittests(self, unittests):
        return [UnitTest(**ut) for ut in unittests]

    def _get_item(self, data):
        common_kwargs = {
            "type": data.get("type"),
            "text": data.get("text"),
            "grade": data.get("grade"),
            "allow_proportion": data.get("allow_proportion", False)
        }

        type_ = common_kwargs["type"]

        if type_ in [SINGLE, MULTIPLE]:
            return ChoiceItem(
                **common_kwargs,
                choices=self._get_choices(data.get("choices", []))
            )

        common_kwargs["min_similar_percent"] = data.get("min_similar_percent", 0)
        common_kwargs["correct_answer"] = data.get("correct_answer")

        if type_ in [SHORT, FULL]:
            return TextItem(
                **common_kwargs
            )

        common_kwargs["language"] = data.get("language")

        if type_ == SCRIPT:
            return ScriptItem(
                **common_kwargs
            )

        if type_ == SCRIPT_UNITTEST:
            return ScriptUnitTestItem(
                **common_kwargs,
                public_unittests=self._get_unittests(data.get("public_unittests", [])),
                private_unittests=self._get_unittests(data.get("private_unittests", []))
            )

        return None

    def _get_index(self, length):
        index = self.context.get("index", None)
        if index is None:
            raise ValidationError("Index must be provided.")

        if index >= length:
            raise ValidationError("Index must be less than the number of items.")

        return index

class ItemSerializer(BaseItemSerializer):
    def create(self, validated_data):
        test_item = TestDocument.objects.filter(id=self.context["test_id"]).first()
        if test_item is None:
            raise ValidationError("Test not found.")

        item = self._get_item(validated_data)

        test_item.items.append(item)
        test_item.save()
        return item

    def update(self, instance, validated_data):
        index = self._get_index(len(instance.items))
        item = self._get_item(validated_data)
        instance.items[index] = item
        instance.save()

        return item

def get_test_grade(obj):
    doc = TestDocument.objects.get(pk=obj.id)

    grade = 0
    for item in doc.items:
        grade += item.grade

    return grade

class TestSerializer(CamelCaseModelSerializer):
    owner = UserProfileSerializer(read_only=True, source="owner.userprofile")
    items = serializers.SerializerMethodField(read_only=True)
    grade = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Test
        fields = ["id", "owner", "created_date", "title", "description", "is_public", "can_share", "auto_check",
                  "items", "show_result", "show_correct", "grade"]
        read_only_fields = ["id", "created_date"]


    def get_grade(self, obj):
       return get_test_grade(obj)

    def get_items(self, obj):
        item = TestDocument.objects.filter(id=obj.id).first()
        if item:
            return ItemSerializer(item.items, many=True).data

        return []

    def validate(self, data):
        if data.get("can_share") is False and self.instance.can_share is True:
            data["is_public"] = False
        if data.get("is_public") is True:
            data["can_share"] = True

        return data