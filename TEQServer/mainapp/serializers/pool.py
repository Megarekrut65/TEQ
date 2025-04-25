from rest_framework import serializers

from mainapp.models.pool import TestPool, TestCategory
from mainapp.serializers.test import BaseItemSerializer
from utility.case_serializers import CamelCaseSerializer, CamelCaseModelSerializer


class ChoiceSerializer(CamelCaseSerializer):
    text = serializers.CharField(max_length=200, allow_blank=True)
    is_correct = serializers.BooleanField(default=False)

class ItemSerializer(BaseItemSerializer):

    def create(self, validated_data):
        category = self.context["category"]

        item = self._get_item(validated_data)

        category.items.append(item)
        category.save()

        return item

    def update(self, instance, validated_data):
        index = self._get_index(len(instance.items))
        item = self._get_item(validated_data)
        instance.items[index] = item
        instance.save()

        return item

class CategorySerializer(CamelCaseSerializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=100)
    items = serializers.SerializerMethodField(read_only=True)

    def get_items(self, obj):
        item = TestCategory.objects.filter(id=obj.id).first()
        if item:
            return ItemSerializer(item.items, many=True).data

        return []

    def create(self, validated_data):
        pool = self.context["pool"]

        category = TestCategory.objects.create(pool_id=pool.id, name=validated_data["name"])

        return category

    def update(self, instance, validated_data):
        instance.name = validated_data["name"]
        instance.save()

        return instance

class PoolSerializer(CamelCaseModelSerializer):
    categories = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TestPool
        fields = ["categories"]

    def get_categories(self, obj):
        categories = TestCategory.objects.filter(pool_id=obj.id).all()
        return CategorySerializer(categories, many=True).data