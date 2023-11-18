from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from user.views import *

urlpatterns = [
    path("register/", RegisterAPIView.as_view()), # post - 회원가입
    path("login/", LoginAPIView.as_view()), # post - 로그인
    path("logout/", LogoutAPIView.as_view()), # post - 로그아웃

    path('google/login/', googleLogin.as_view(), name='google_login'), # get - 구글 로그인
    path('google/callback/', googleCallback.as_view(), name='google_callback'), # get - 구글 콜백

    path("kakao/login/", kakaoLogin), # get - 카카오 로그인
    path("kakao/callback/", kakaoCallback), # get - 카카오 콜백
    path("naver/login/", naverLogin), # get - 네이버 로그인
    path("naver/callback/", naverCallback), # get - 네이버 콜백
]
