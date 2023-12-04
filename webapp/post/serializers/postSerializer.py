from post.models import Post, PostImage
from post.serializers.postImageSerializer import PostImageSerializer
from rest_framework import serializers

from user.models import User


class PostSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    user = serializers.CharField(source='user.username', required=False)
    like = serializers.SerializerMethodField(read_only=True)
    view = serializers.SerializerMethodField(read_only=True)
    def get_images(self, obj):
        images = obj.image.all()
        return PostImageSerializer(instance=images, many=True, context=self.context).data

    def get_like(self, obj):
        return obj.like

    def get_view(self, obj):
        return obj.view

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'content',
            'created_at',
            'view',
            'like',
            'images',
            'is_anonymous',
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user', None)

        if user_data and 'username' in user_data:
            username = user_data['username']
            user_instance, created = User.objects.get_or_create(username=username)
            validated_data['user'] = user_instance

        instance = Post.objects.create(**validated_data)

        img_set = self.context['request'].FILES
        for img_data in img_set.getlist('image'):
            PostImage.objects.create(post=instance, image=img_data)
        return instance

