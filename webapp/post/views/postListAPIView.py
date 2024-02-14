from post.models import Post
from post.serializers import PostSerializer

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status, pagination

from django.db.models import Q
from rest_framework.filters import BaseFilterBackend

class CustomSearchFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        search_title = request.query_params.get('search_title', None)
        search_content = request.query_params.get('search_content', None)
        search_all = request.query_params.get('search_all', None)

        if search_title is not None:
            queryset = queryset.filter(title__icontains=search_title)

        if search_content is not None:
            queryset = queryset.filter(content__icontains=search_content)

        if search_all is not None:
            queryset = queryset.filter(Q(title__icontains=search_all) | Q(content__icontains=search_all))

        return queryset

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = pagination.PageNumberPagination
    filter_backends = [CustomSearchFilter]
    # ordering_fields = ['created_at']

    # 게시글 작성
    def post(self, request):
        serializer = PostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
