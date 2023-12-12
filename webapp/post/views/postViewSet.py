import datetime

from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from post.models import Post, PostTag
from post.serializers.postSerializer import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            for item in serializer.data:
                post_tags = PostTag.objects.filter(post__id=item['id'])
                tags = [post_tag.tag.name for post_tag in post_tags]
                item['tags'] = tags
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        for item in data:
            post_tags = PostTag.objects.filter(post__id=item['id'])
            tags = [post_tag.tag.name for post_tag in post_tags]
            item['tags'] = tags

        return Response(data)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(self.get_queryset(), pk=pk)

        # 유효기간 하루
        expires = timezone.now() + datetime.timedelta(days=1)

        serializer = self.get_serializer(post)
        data = serializer.data
        post_tags = PostTag.objects.filter(post=post)
        tags = []
        for post_tag in post_tags:
            tags.append(post_tag.tag.name)
        data['tags'] = tags
        response = Response(data, status=HTTP_200_OK)

        # 기존 쿠키에 view 있나 확인
        if 'view' in request.COOKIES:
            cookies = request.COOKIES['view']
            cookies_list = cookies.split('|')

            # 기존 쿠키 리스트에 정보가 없으면 조회수 1 증가
            if str(pk) not in cookies_list:
                response.set_cookie('view', cookies + f'|{pk}', expires=expires)
                post.view += 1
                post.save()
        else:
            response.set_cookie('view', pk, expires=expires)
            post.view += 1
            post.save()

        return response