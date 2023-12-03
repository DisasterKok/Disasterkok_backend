from post.models import Post, PostImage
from post.serializers.postImageSerializer import PostImageSerializer
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    like = serializers.SerializerMethodField(read_only=True)
    # view = ViewSerializer(many=True, read_only=True)
    def get_images(self, obj):
        images = obj.image.all()
        return PostImageSerializer(instance=images, many=True, context=self.context).data

    def get_user(self, obj):
        return str(obj.user)

    def get_like(self, obj):
        return obj.like

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'content',
            'created_at',
            # 'view',
            'like',
            'images',
            'is_anonymous',
        ]

    def create(self, validated_data):
        instance = Post.objects.create(**validated_data)
        img_set = self.context['request'].FILES
        for img_data in img_set.getlist('image'):
            PostImage.objects.create(post=instance, image=img_data)
        return instance

