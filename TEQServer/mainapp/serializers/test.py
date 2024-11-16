from rest_framework import serializers
from mainapp.models.test import Test
from mainapp.serializers.user import UserProfileSerializer

class TestSerializer(serializers.ModelSerializer):
    owner = UserProfileSerializer(read_only=True)

    class Meta:
        model = Test
        fields = ["id", "owner", "created_date", "title", "description", "is_public"]
        read_only_fields = ["id", "owner", "created_date"]

#
# class AnswerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Answer
#         fields = ["id", "text", "is_correct"]
#
#
# class SingleAnswerItemSerializer(serializers.ModelSerializer):
#     answers = AnswerSerializer(many=True)
#
#     class Meta:
#         model = SingleAnswerItem
#         fields = ["id", "test", "question_text", "answers"]
#         write_only_fields = ["test"]
#
# class MultipleAnswerItemSerializer(serializers.ModelSerializer):
#     answers = AnswerSerializer(many=True)
#
#     class Meta:
#         model = MultipleAnswerItem
#         fields = ["id", "test", "question_text", "answers"]
#         write_only_fields = ["test"]
#
#
# class TextAnswerItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TextAnswerItem
#         fields = ["id", "test", "question_text"]
#         write_only_fields = ["test"]
#
#
# class ItemSerializer(serializers.Serializer):
#     type = serializers.ChoiceField(choices=["single", "multiple", "text"])
#     question_text = serializers.CharField()
#     correct_answer = serializers.CharField(required=False)
#     answers = AnswerSerializer(many=True, required=False)
#
#     def create(self, validated_data):
#         test = validated_data.pop("test")
#         item_type = validated_data.pop("type")
#
#         if item_type == "single":
#             item = SingleAnswerItem.objects.create(test=test, **validated_data)
#         elif item_type == "multiple":
#             item = MultipleAnswerItem.objects.create(test=test, **validated_data)
#         elif item_type == "text":
#             item = TextAnswerItem.objects.create(test=test, **validated_data)
#         else:
#             raise serializers.ValidationError("Invalid item type")
#
#         return item
#
# class TestDetailSerializer(serializers.ModelSerializer):
#     items = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Test
#         fields = ["id", "owner", "created_date", "title", "description", "is_public", "items"]
#
#     def get_items(self, obj):
#         items = []
#         single_items = SingleAnswerItem.objects.filter(test=obj)
#         multiple_items = MultipleAnswerItem.objects.filter(test=obj)
#         text_items = TextAnswerItem.objects.filter(test=obj)
#
#         for item in single_items:
#             items.append(SingleAnswerItemSerializer(item).data)
#
#         for item in multiple_items:
#             items.append(MultipleAnswerItemSerializer(item).data)
#
#         for item in text_items:
#             items.append(TextAnswerItemSerializer(item).data)
#
#         return items