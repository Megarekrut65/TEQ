from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_mongoengine import serializers as mg_serializers

from mainapp.item_types import ITEM_TYPES, SINGLE, MULTIPLE, TEXT
from mainapp.models.answer import Answer, AnswerDocument, AnswerChoiceItem, AnswerTextItem
from mainapp.models.test import Test, TestDocument
from userapp.serializers import UserProfileSerializer
from utility.case_serializers import CamelCaseSerializer, CamelCaseModelSerializer


class ChoiceSerializer(CamelCaseSerializer):
    text = serializers.CharField(max_length=200, allow_blank=True)

class ItemSerializer(CamelCaseSerializer):
    test_id = serializers.UUIDField(write_only=True)

    text = serializers.CharField(max_length=500, allow_blank=True)
    type = serializers.ChoiceField(choices=ITEM_TYPES)
    choices = ChoiceSerializer(many=True, required=False)

class TestSerializer(CamelCaseModelSerializer):
    owner = UserProfileSerializer(read_only=True, source="owner.userprofile")
    items = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Test
        fields = ["id", "owner", "created_date", "title", "description", "items"]
        read_only_fields = ["id", "created_date"]

    def get_items(self, obj):
        item = TestDocument.objects.filter(id=obj.id).first()
        if item:
            return ItemSerializer(item.items, many=True).data

        return []

class AnswerItemSerializer(CamelCaseSerializer):
    type = serializers.ChoiceField(choices=ITEM_TYPES)
    choices = serializers.ListField(
        child=serializers.IntegerField(min_value=0), required=False, allow_null=True, allow_empty=True
    )
    answer = serializers.CharField(max_length=5000, required=False, allow_blank=True, allow_null=True)

    def create(self, validated_data):
        item = None
        if validated_data["type"] in [SINGLE, MULTIPLE]:
            item = AnswerChoiceItem(
                type=validated_data["type"],
                choices=validated_data["choices"],
            )
        elif validated_data["type"] == TEXT:
            item = AnswerTextItem(
                type=validated_data["type"],
                answer=validated_data["answer"]
            )

        return item


class AnswerSerializer(CamelCaseModelSerializer):
    items = serializers.SerializerMethodField()
    test = TestSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ["id", "owner", "pass_date", "version", "items", "test", "checked", "auto_checked", "agree"]
        read_only_fields = ["id", "pass_date", "owner", "version", "checked", "auto_checked", "agree"]

    def get_items(self, obj):
        doc = AnswerDocument.objects.get(pk=obj.id)
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

        test_doc = TestDocument.objects.filter(id=validated_data["test"].id).first()
        test_items = test_doc.items

        self._validate_items(test_items, validated_items)

        answer = Answer.objects.create(
            owner=validated_data["owner"],
            version=validated_data["version"],
            test=validated_data["test"],)

        doc = AnswerDocument.objects.create(id=answer.id, items=validated_items,
                                            test_items=test_items)

        return answer