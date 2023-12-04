from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from post.models import Post, PostLike

class PostLikeAPIView(APIView):
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        user = self.request.user

        post_liked = PostLike.objects.filter(user=user, post_id=post_id).first()
        if post_liked:
            post_liked.delete()
            post = Post.objects.get(id=post_id)
            post.like -= 1
            post.save()
            return Response({'message': '좋아요 취소'}, status=status.HTTP_200_OK)
        else:
            post_like = PostLike(user=user, post_id=post_id)
            post_like.save()
            post = Post.objects.get(id=post_id)
            post.like += 1
            post.save()

        return Response({'message': '좋아요'}, status=status.HTTP_201_CREATED)