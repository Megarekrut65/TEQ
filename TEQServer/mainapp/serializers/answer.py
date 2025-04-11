from rest_framework import serializers

from mainapp.item_types import ITEM_TYPES
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