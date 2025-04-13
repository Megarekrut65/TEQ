from mongoengine import DoesNotExist
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from mainapp.item_types import ITEM_TYPES, TEXT, SINGLE, MULTIPLE
from mainapp.models.test import Test, TestDocument, ChoiceItem, Choice, TextItem
from userapp.serializers import UserProfileSerializer
from utility.case_serializers import CamelCaseSerializer, CamelCaseModelSerializer


class ChoiceSerializer(CamelCaseSerializer):
    text = serializers.CharField(max_length=200, allow_blank=True)
    is_correct = serializers.BooleanField(default=False)

class ItemSerializer(CamelCaseSerializer):
    test_id = serializers.UUIDField(write_only=True)

    text = serializers.CharField(max_length=500, allow_blank=True)
    type = serializers.ChoiceField(choices=ITEM_TYPES)
    grade = serializers.FloatField(min_value=0.0)
    allow_proportion = serializers.BooleanField(default=False)

    choices = ChoiceSerializer(many=True, required=False)

    min_similar_percent = serializers.FloatField(required=False, min_value=0, max_value=100)
    correct_answer = serializers.CharField(max_length=5000, required=False, allow_blank=True, allow_null=True)

    def validate(self, data):
        question_type = data.get("type")
        choices = data.get("choices", [])
        count = len(choices)

        if question_type == TEXT:
            return data

        if count < 1:
            raise ValidationError("At least one choices are required.")

        if question_type == SINGLE:
            correct = len([choice for choice in choices if choice["is_correct"]])
            if correct < 0:
                raise ValidationError("Exactly one choice must be marked as correct.")

        return data

    def validate_test_id(self, value):
        try:
            TestDocument.objects.get(id=value)
        except DoesNotExist:
            raise ValidationError("TestItem with this ID does not exist.")
        return value

    def __get_item(self, validated_data):
        item = None
        if validated_data["type"] in [SINGLE, MULTIPLE]:
            item = ChoiceItem(
                type=validated_data["type"],
                text=validated_data["text"],
                grade=validated_data["grade"],
                allow_proportion=validated_data["allow_proportion"],
                choices=[
                    Choice(text=choice["text"], is_correct=choice["is_correct"])
                    for choice in validated_data["choices"]
                ]
            )
        elif validated_data["type"] == TEXT:
            item = TextItem(
                type=validated_data["type"],
                text=validated_data["text"],
                grade=validated_data["grade"],
                allow_proportion=validated_data["allow_proportion"],
                min_similar_percent=validated_data["min_similar_percent"],
                correct_answer=validated_data["correct_answer"]
            )

        return item

    def create(self, validated_data):
        test_item = TestDocument.objects.get(id=self.validated_data["test_id"])

        item = self.__get_item(validated_data)

        test_item.items.append(item)
        test_item.save()
        return item

    def update(self, instance, validated_data):
        test_item = TestDocument.objects.get(id=self.validated_data["test_id"])

        index = self.context.get("index", None)
        if index is None:
            raise ValidationError("Index must be provided.")

        if index >= len(test_item.items):
            raise ValidationError("Index must be less than the number of items.")

        item = self.__get_item(validated_data)
        test_item.items[index] = item
        test_item.save()

        return item

class TestSerializer(CamelCaseModelSerializer):
    owner = UserProfileSerializer(read_only=True, source="owner.userprofile")
    items = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Test
        fields = ["id", "owner", "created_date", "title", "description", "is_public", "auto_check",
                  "items"]
        read_only_fields = ["id", "created_date"]

    def get_items(self, obj):
        item = TestDocument.objects.filter(id=obj.id).first()
        if item:
            return ItemSerializer(item.items, many=True).data

        return []