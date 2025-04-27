from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from mainapp.item_types import ITEM_TYPES, SINGLE, MULTIPLE, SHORT, FULL
from mainapp.models.answer import Answer, AnswerDocument, AnswerChoiceItem, AnswerTextItem
from mainapp.models.test import TestDocument
from mainapp.serializers.safe_test import SafeTestSerializer, SafeItemSerializer
from mainapp.serializers.test import get_test_grade, ItemSerializer
from userapp.serializers import UserProfileSerializer
from utility.case_serializers import CamelCaseSerializer, CamelCaseModelSerializer


class AnswerItemSerializer(CamelCaseSerializer):
    type = serializers.ChoiceField(choices=ITEM_TYPES)
    choices = serializers.ListField(
        child=serializers.IntegerField(), required=False, allow_null=True, allow_empty=True
    )
    answer = serializers.CharField(max_length=5000, required=False, allow_blank=True, allow_null=True)
    grade = serializers.FloatField(read_only=True)
    similarity = serializers.FloatField(read_only=True, required=False, allow_null=True)


    def __get_item(self, validated_data):
        item = None
        if validated_data["type"] in [SINGLE, MULTIPLE]:
            item = AnswerChoiceItem(
                type=validated_data["type"],
                choices=validated_data["choices"],
            )
        elif validated_data["type"] in [SHORT, FULL]:
            item = AnswerTextItem(
                type=validated_data["type"],
                answer=validated_data["answer"]
            )

        return item

    def create(self, validated_data):
       return self.__get_item(validated_data)

class AnswerItemGradeSerializer(CamelCaseSerializer):
    grade = serializers.FloatField()

    def update(self, instance, validated_data):
        answer_item = AnswerDocument.objects.get(id=self.context.get("answer_id", None))

        index = self.context.get("index", None)
        if index is None:
            raise ValidationError("Index must be provided.")

        if index >= len(answer_item.items):
            raise ValidationError("Index must be less than the number of items.")

        item = answer_item.items[index]
        item.grade = self.validated_data["grade"]
        answer_item.save()

        return item

class AnswerCheckSerializer(CamelCaseModelSerializer):
    class Meta:
        model = Answer
        fields = ["checked"]

class AnswerSerializer(CamelCaseModelSerializer):
    items = serializers.SerializerMethodField()
    test_items = serializers.SerializerMethodField()
    test = SafeTestSerializer(read_only=True)
    owner = UserProfileSerializer(read_only=True, source="owner.userprofile")
    grade = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Answer
        fields = ["id", "owner", "pass_date", "version", "items", "test", "checked",
                  "auto_checked", "agree", "show_correct", "grade", "max_grade", "test_items", "owner"]
        read_only_fields = ["id", "pass_date", "owner", "version", "checked", "auto_checked",
                            "agree", "max_grade"]

    def get_test_items(self, obj):
        doc = AnswerDocument.objects.filter(id=obj.id).first()
        if doc is None:
            return []

        items = doc.test_items

        if obj.test.show_correct or self.context.get("is_owner", False):
            return ItemSerializer(items, many=True).data

        return SafeItemSerializer(items, many=True).data

    def get_grade(self, obj):
        doc = AnswerDocument.objects.filter(id=obj.id).first()
        if doc is None:
            return 0

        grade = 0
        for item in doc.items:
            grade += item.grade

        return grade

    def get_items(self, obj):
        doc = AnswerDocument.objects.filter(id=obj.id).first()
        if doc is None:
            return []

        return AnswerItemSerializer(doc.items, many=True).data

    def _validate_items(self, test_items, validated_items):
        if len(test_items) != len(validated_items):
            raise serializers.ValidationError({"items": "There must be all answers"})

        for i in range(len(validated_items)):
            if validated_items[i].type != test_items[i].type:
                raise serializers.ValidationError({"items": "Type mismatch"})

    def create(self, validated_data):
        items = self.initial_data.get("items")
        if items is None:
            raise serializers.ValidationError({"items": "This field is required."})
        item_serializer = AnswerItemSerializer(data=items, many=True)
        item_serializer.is_valid(raise_exception=True)
        validated_items = item_serializer.create(item_serializer.validated_data)

        test = validated_data["test"]
        test_doc = TestDocument.objects.filter(id=test.id).first()
        test_items = test_doc.items

        self._validate_items(test_items, validated_items)

        answer = Answer.objects.create(
            owner=validated_data["owner"],
            version=validated_data["version"],
            test=test, show_correct=test.show_correct, max_grade=get_test_grade(test))

        doc = AnswerDocument.objects.create(id=answer.id, items=validated_items,
                                            test_items=test_items)

        return answer