from post.models import Post
from post.serializers import PostSerializer

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status, pagination

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = pagination.PageNumberPagination

    # 게시글 작성
    def post(self, request):
        serializer = PostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
