from requests import Response
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from post.models import Post
from post.serializers import PostSerializer


# url 연결 안함
@permission_classes([AllowAny])
class PostHomeViewSet(viewsets.ViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        sorted_posts = sorted(
            serializer.data,
            key=lambda post: post['created_at'],
            reverse=True
        )
        home_posts = sorted_posts[:6]

        return Response(home_posts)

