from post.models import Post, PostImage, PostTag, Tag
from post.serializers.postImageSerializer import PostImageSerializer
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    like = serializers.SerializerMethodField(read_only=True)
    view = serializers.SerializerMethodField(read_only=True)
    tags = serializers.ListSerializer(child=serializers.CharField(max_length=10), required=False)

    def get_images(self, obj):
        images = obj.image.all()
        return PostImageSerializer(instance=images, many=True, context=self.context).data

    def get_user(self, obj):
        return str(obj.user)

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
            'tags',
        ]

    def create(self, validated_data):
        # Extract tags from validated data
        tag_set = validated_data.pop('tags', [])

        # Create the Post instance
        post = Post.objects.create(**validated_data)

        # Get image set from request
        img_set = self.context['request'].FILES.getlist('image')

        # Create PostImage instances
        for img in img_set:
            PostImage.objects.create(post=post, image=img)

        # Create PostTag instances
        for tag in tag_set:
            tag_instance, _ = Tag.objects.get_or_create(name=tag)
            PostTag.objects.create(post=post, tag=tag_instance)

        return post