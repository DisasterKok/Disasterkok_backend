import os, requests

from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User


@api_view(["GET"])
@permission_classes([AllowAny])
def kakaoLogin(request):
    REST_API = os.environ.get("KAKAO_REST_API")
    REDIRECT_URL = os.environ.get("KAKAO_REDIRECT_URL")
    url = f'https://kauth.kakao.com/oauth/authorize?client_id={REST_API}&redirect_uri={REDIRECT_URL}&response_type=code'
    return redirect(url)

@api_view(["GET"])
@permission_classes([AllowAny])
def kakaoCallback(request):
    url = "https://kauth.kakao.com/oauth/token"
    code = request.GET.get("code")

    if code is None:
        raise Exception("code is None")

    data = {
        'grant_type': 'authorization_code',
        'client_id': os.environ.get("KAKAO_REST_API"),
        'redirect_uri': os.environ.get("KAKAO_REDIRECT_URL"),
        'code': code,
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    }

    token_request = requests.post(url, data=data, headers=headers)
    token_json = token_request.json()

    if 'access_token' in token_json:
        access_token = token_json["access_token"]
        # access_token = token_response.json().get('access_token')
        url = "https://kapi.kakao.com/v2/user/me"
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        }
        profile_request = requests.get(url, headers=headers)
        profile_json = profile_request.json()

        kakaoId = profile_json.get('id')
        username = profile_json['properties']['nickname']

        if kakaoId is not None:
            if User.objects.filter(kakaoId=kakaoId).exists():
                user = User.objects.get(kakaoId=kakaoId)
                refresh = RefreshToken.for_user(user)
                data = {
                    "user": {
                        "id": user.id,
                        "kakaoId": user.kakaoId,
                        "username": user.username,
                    },
                    "token": {
                        "access": f"{str(refresh.access_token)}",
                        "refresh": f"{str(refresh)}"
                    }
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                User(kakaoId=kakaoId, username=username).save()
                user = User.objects.get(kakaoId=kakaoId)
                refresh = RefreshToken.for_user(user)
                data = {
                    "user": {
                        "id": user.id,
                        "kakaoId": user.kakaoId,
                        "username": user.username,
                    },
                    "token": {
                        "access": f"{str(refresh.access_token)}",
                        "refresh": f"{str(refresh)}"
                    }
                }
                return Response(data, status=status.HTTP_200_OK)
    return Response({"message": "kakao에서 정보를 불러오지 못했습니다."}, status=status.HTTP_400_BAD_REQUEST)