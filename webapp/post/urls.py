from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register(r'post', PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('post/<int:post_id>/likes/', PostLikeAPIView.as_view(), name='likes'),
    path('top/', PostHomeViewSet.as_view({'get': 'list'}), name='top'),
    path('tag/', PostTagAPIView.as_view(), name='tag'),
]

# post-list: /posts/post/ ({'get': 'list', 'post': 'create'})
# post-detail: /posts/post/<pk>/ ({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})