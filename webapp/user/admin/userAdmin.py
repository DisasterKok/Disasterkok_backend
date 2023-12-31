from django.contrib import admin

from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'username',
    '__str__',
    'created_at',
    'updated_at',
    'nickname',
    'email',
  )