from post.models import Post, PostTag
from post.serializers import PostSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import datetime
from django.shortcuts import get_object_or_404
from django.utils import timezone

class PostDetailAPIView(APIView):
    def get_object(self, post_id):
        return get_object_or_404(Post, id=post_id)

    # def get_object(self, post_id):
    #     try:
    #         return Post.objects.get(id=post_id)
    #     except Post.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    # 게시글 상세 조회
    def get(self, request, post_id):
        # post = Post.objects.get(id=post_id)
        # serializer = PostSerializer(post)
        # post = get_object_or_404(self.get_queryset(), pk=pk)

        post = self.get_object(post_id)

        # serializer = self.get_serializer(post)
        serializer = PostSerializer(post)
        data = serializer.data
        post_tags = PostTag.objects.filter(post=post)
        tags = []
        for post_tag in post_tags:
            tags.append(post_tag.tag.name)
        data['tags'] = tags
        response = Response(data, status=status.HTTP_200_OK)

        # 유효기간 하루
        expires = timezone.now() + datetime.timedelta(days=1)

        # 기존 쿠키에 view 있나 확인
        if 'view' in request.COOKIES:
            cookies = request.COOKIES['view']
            cookies_list = cookies.split('|')
            print(cookies_list)

            # 기존 쿠키 리스트에 정보가 없으면 조회수 1 증가
            if str(post_id) not in cookies_list:
                response.set_cookie('view', cookies + f'|{post_id}', expires=expires)
                post.view += 1
                post.save()
        else:
            response.set_cookie('view', str(post_id), expires=expires)
            post.view += 1
            post.save()

        return response
        # return Response(serializer.data, status=status.HTTP_200_OK)

    # 게시글 삭제
    def delete(self, request, post_id):
        # post = Post.objects.get(id=post_id)
        post = self.get_object(post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # # 게시글 조회수
    # def retrieve(self, request, pk=None):
    #     post = get_object_or_404(self.get_queryset(), pk=pk)
    #
    #     # 유효기간 하루
    #     expires = timezone.now() + datetime.timedelta(days=1)
    #
    #     serializer = self.get_serializer(post)
    #     data = serializer.data
    #     post_tags = PostTag.objects.filter(post=post)
    #     tags = []
    #     for post_tag in post_tags:
    #         tags.append(post_tag.tag.name)
    #     data['tags'] = tags
    #     response = Response(data, status=status.HTTP_200_OK)
    #
    #     # 기존 쿠키에 view 있나 확인
    #     if 'view' in request.COOKIES:
    #         cookies = request.COOKIES['view']
    #         cookies_list = cookies.split('|')
    #
    #         # 기존 쿠키 리스트에 정보가 없으면 조회수 1 증가
    #         if str(pk) not in cookies_list:
    #             response.set_cookie('view', cookies + f'|{pk}', expires=expires)
    #             post.view += 1
    #             post.save()
    #     else:
    #         response.set_cookie('view', pk, expires=expires)
    #         post.view += 1
    #         post.save()
    #
    #     return response