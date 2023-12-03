from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post.views.postViewSet import PostViewSet
from post.views.postLikeAPIView import PostLikeAPIView

router = DefaultRouter()
router.register(r'post', PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('post/<int:post_id>/likes/', PostLikeAPIView.as_view(), name='likes'),
]

# post-list: /posts/post/ ({'get': 'list', 'post': 'create'})
# post-detail: /posts/post/<pk>/ ({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
