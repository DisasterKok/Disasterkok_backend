# import os
#
# from django.shortcuts import redirect
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
#
# from user.models import User
#
# @api_view(["GET", "POST"])
# @permission_classes([AllowAny])
# def googleLogin(request):
#     CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
#     REDIRECT_URI = os.environ.get("GOOGLE_REDIRECT_URL")
#     print(REDIRECT_URI)
#     STATE = "RANDOM_STATE"
#     url = f"https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&state={STATE}&scope=email profile"
#     return redirect(url)
#
#
# # @api_view["GET", "POST"]
#
# def googleCallback(request):
#     print("success")
#     return redirect("https://www.google.com")
#
