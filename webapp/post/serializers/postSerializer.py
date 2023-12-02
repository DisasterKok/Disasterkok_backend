from post.models import Post, PostImage
from post.serializers.postImageSerializer import PostImageSerializer
from user.serializers import userSerializer
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    user = userSerializer
    image = PostImageSerializer(many=True, read_only=True)

    def get_image(self, obj):
        image = obj.image.all()
        serializer = PostImageSerializer(image, many=True, context=self.context)
        return serializer.data

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'content',
            'created_at',
            'image',
        ]

    def create(self, validated_data):
        posts = Post.objects.create(**validated_data)
        img_set = self.context['request'].FILES
        for img in img_set.getlist('image'):
            PostImage.objects.create(post=posts, image=img)
        return posts

