from django.urls import path

from user.views import *

urlpatterns = [
    path("register/", RegisterAPIView.as_view()), # post - 회원가입
]