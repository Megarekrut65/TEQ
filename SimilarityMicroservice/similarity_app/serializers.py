from rest_framework import serializers

from utility.case_serializers import CamelCaseSerializer


class SimilaritySerializer(CamelCaseSerializer):
    text1 = serializers.CharField()
    text2 = serializers.CharField()

