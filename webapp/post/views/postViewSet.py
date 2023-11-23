from rest_framework.viewsets import ModelViewSet

from post.models import Post
from post.serializers.postSerializer import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
