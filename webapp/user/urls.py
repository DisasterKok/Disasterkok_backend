from django.urls import path

from user.views import *

urlpatterns = [
    path("register/", RegisterAPIView.as_view()), # post - 회원가입
    path("login/", LoginAPIView.as_view()), # post - 로그인
    path("logout/", LogoutAPIView.as_view()), # post - 로그아웃
]
