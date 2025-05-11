from rest_framework import serializers

from mainapp.item_types import ITEM_TYPES
from mainapp.models.test import Test, TestDocument
from mainapp.serializers.test import UnitTestSerializer
from mainapp.unit_types import UNIT_TYPES
from userapp.serializers import UserProfileSerializer
from utility.case_serializers import CamelCaseSerializer, CamelCaseModelSerializer


class SafeChoiceSerializer(CamelCaseSerializer):
    text = serializers.CharField(max_length=200, allow_blank=True)

class SafeItemSerializer(CamelCaseSerializer):
    test_id = serializers.UUIDField(write_only=True)

    text = serializers.CharField(max_length=500, allow_blank=True)
    type = serializers.ChoiceField(choices=ITEM_TYPES)
    choices = SafeChoiceSerializer(many=True, required=False)

    language = serializers.CharField(max_length=50, required=False, allow_blank=True, allow_null=True)

    public_unittests = UnitTestSerializer(many=True, required=False)
    function_structure = serializers.CharField(max_length=500, required=False, allow_blank=True, allow_null=True)
    function_type = serializers.ChoiceField(choices=UNIT_TYPES, required=False, allow_blank=True, allow_null=True)

class SafeTestSerializer(CamelCaseModelSerializer):
    owner = UserProfileSerializer(read_only=True, source="owner.userprofile")
    items = serializers.SerializerMethodField()


    class Meta:
        model = Test
        fields = ["id", "owner", "created_date", "title", "description", "category", "show_correct", "items", "answer_count"]
        read_only_fields = ["id", "created_date"]

    def get_items(self, obj):
        return []

class PassTestSerializer(SafeTestSerializer):

    def get_items(self, obj):
        item = TestDocument.objects.filter(id=obj.id).first()
        if item:
            return SafeItemSerializer(item.items, many=True).data

        return []