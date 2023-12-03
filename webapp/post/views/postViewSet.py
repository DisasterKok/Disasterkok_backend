from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.viewsets import ModelViewSet

from post.models import Post
from post.serializers.postSerializer import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    def get_permissions(self):
        permission_classes = []

        if self.action in ['update', 'retrieve']:
            permission_classes = [IsAdminUser]
        elif self.action in ['create']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['list']:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]
