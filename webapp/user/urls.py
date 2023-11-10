from django.urls import path

from user.views import *

urlpatterns = [
    path("register/", RegisterAPIView.as_view()), # post - 회원가입
    path("login/", LoginAPIView.as_view()), # post - 로그인
    path("logout/", LogoutAPIView.as_view()), # post - 로그아웃
    # path("google/login/", googleLogin),
    # path("google/callback/", googleCallback),
    path("kakao/login/", kakaoLogin), # get - 카카오 로그인
    path("kakao/callback/", kakaoCallback), # get - 카카오 콜백
]
