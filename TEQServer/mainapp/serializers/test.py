from tkinter.constants import MULTIPLE

from mongoengine import DoesNotExist
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from mainapp.models.test import Test, TestItem, ChoiceAnswerItem, Choice, TextAnswerItem
from mainapp.serializers.case_serializers import CamelCaseSerializer, CamelCaseModelSerializer
from mainapp.serializers.user import UserProfileSerializer



class TestSerializer(CamelCaseModelSerializer):
    owner = UserProfileSerializer(read_only=True)
    items = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Test
        fields = ["id", "owner", "created_date", "title", "description", "is_public", "items"]
        read_only_fields = ["id", "created_date"]

    def get_items(self, obj):
        item = TestItem.objects.filter(id=obj.id).first()
        if item:
            return item.items

        return []


class ChoiceSerializer(CamelCaseSerializer):
    text = serializers.CharField(max_length=200)
    is_correct = serializers.BooleanField(default=False)

class ItemSerializer(CamelCaseSerializer):
    SINGLE = "SINGLE"
    MULTIPLE = "MULTIPLE"
    TEXT = "TEXT"
    TYPES = [SINGLE, MULTIPLE, TEXT]

    test_id = serializers.UUIDField()
    text = serializers.CharField(max_length=500)
    type = serializers.ChoiceField(choices=TYPES)
    choices = ChoiceSerializer(many=True, required=False)
    correct_answer = serializers.CharField(max_length=5000, required=False, allow_null=True)

    def validate(self, data):
        question_type = data.get("type")
        choices = data.get("choices", [])
        count = len(choices)

        if question_type == self.TEXT:
            if count > 0:
                raise ValidationError(f"For '{self.TEXT}' type questions, no choices are allowed.")
            return data

        if count < 2:
            raise ValidationError("At least two choices are required.")

        if question_type == self.SINGLE:
            correct = len([choice for choice in choices if choice["is_correct"]])
            if correct != 1:
                raise ValidationError("Exactly one choice must be marked as correct.")

        return data

    def validate_test_id(self, value):
        try:
            TestItem.objects.get(id=value)
        except DoesNotExist:
            raise ValidationError("TestItem with this ID does not exist.")
        return value

    def save(self):
        test_item = TestItem.objects.get(id=self.validated_data["test_id"])

        item = None
        if self.validated_data["type"] in [self.SINGLE, self.MULTIPLE]:
            item = ChoiceAnswerItem(
                type=self.validated_data["type"],
                text=self.validated_data["text"],
                choices=[
                    Choice(text=choice["text"], is_correct=choice["is_correct"])
                    for choice in self.validated_data["choices"]
                ]
            )
        elif self.validated_data["type"] == self.TEXT:
            item = TextAnswerItem(
                type=self.validated_data["type"],
                text=self.validated_data["text"],
                correct_answer=self.validated_data["correct_answer"]
            )

        test_item.items.append(item)
        test_item.save()
        return item
