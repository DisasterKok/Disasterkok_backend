from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post.views.postViewSet import PostViewSet

router = DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# post-list: /posts/post/ ({'get': 'list', 'post': 'create'})
# post-detail: /posts/post/<pk>/ ({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
