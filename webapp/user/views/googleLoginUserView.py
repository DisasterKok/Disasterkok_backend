import jwt
from django.contrib.sites import requests

from user.models import User


def googleLogin(request):
    token = request.headers.get["Authorization"]
    url = 'https://oauth2.googleapis.com/tokeninfo?id_token='
    response = requests.get(url + token)
    user = response.json()
    print(user)
    # googleId = user.get('id')
    #
    # if User.objexts.filter(googleId=googleId).exists():
    #     user_info = User.objects.get(googleId=googleId)
    #     token = jwt.encode({'id': user.id}, SECRET_KEY, algorithm='HS256')
    #     return JsonResponse({'token': token}, status=200)
