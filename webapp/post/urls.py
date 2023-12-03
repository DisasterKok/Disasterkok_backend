from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post.views.postViewSet import PostViewSet
# from post.views.postImageViewSet import PostImageViewSet

router = DefaultRouter()
router.register(r'post', PostViewSet)
# router.register('postimage', PostImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# post-list: /posts/post/ ({'get': 'list', 'post': 'create'})
# post-detail: /posts/post/<pk>/ ({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})

# postimage-list: /posts/postimage/ ({'get': 'list', 'post': 'create'})
# postimage-detail: /posts/postimage/<pk>/ ({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})