import datetime

from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
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

    def retrieve(self, request, pk=None):
        post = get_object_or_404(self.get_queryset(), pk=pk)

        # 유효기간 하루
        expires = timezone.now() + datetime.timedelta(days=1)

        serializer = self.get_serializer(post)
        response = Response(serializer.data, status=HTTP_200_OK)

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