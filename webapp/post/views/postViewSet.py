from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from post.models import Post
from post.serializers.postSerializer import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    def get_permissions(self):
        permission_classes = []

        if self.action in ['update', 'retrieve']:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]
