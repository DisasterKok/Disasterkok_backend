from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate

from region.models import Region
from user.serializers import LoginSerializer

@permission_classes([AllowAny])
class LoginAPIView(APIView):
    def post(self, request):
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password')
        )
        if user is not None:
            serializer = LoginSerializer(user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            regions = Region.objects.filter(notification__user=request.user.id)
            if regions:
                exist = True
            else:
                exist = False

            res = Response(
                {
                    "user": serializer.data,
                    "message": "login success",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                    "exist": exist
                },
                status=status.HTTP_200_OK,
            )
            # jwt 토큰 -> 쿠키에 저장
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)
            return res
        else:
            return Response({"message": "login failed"}, status=status.HTTP_401_UNAUTHORIZED)
