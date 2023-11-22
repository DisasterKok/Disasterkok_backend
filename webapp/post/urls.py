from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post.views.postDetailViewSet import PostDetailViewSet

router = DefaultRouter()
router.register('post', PostDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]