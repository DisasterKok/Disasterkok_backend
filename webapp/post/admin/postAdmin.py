from django.contrib import admin
from post.models import Post, PostImage, PostLike

admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(PostLike)