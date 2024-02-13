from post.models import Post
from post.serializers import PostSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PostListAPIView(APIView):
    # 게시글 목록 조회
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 게시글 작성
    def post(self, request):
        serializer = PostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
