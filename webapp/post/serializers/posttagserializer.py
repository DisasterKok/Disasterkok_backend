from rest_framework import serializers


class PostTagSerializer(serializers.Serializer):
    tags = serializers.ListField()