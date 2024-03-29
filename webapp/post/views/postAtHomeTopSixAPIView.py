from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK

from post.models import Post
from post.serializers import PostSerializer

@permission_classes([AllowAny])
class PostAtHomeTopSixAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        sorted_posts = sorted(
            serializer.data,
            key=lambda post: post['created_at'],
            reverse=True
        )
        home_posts = sorted_posts[:6]

        return Response(home_posts, status=HTTP_200_OK)