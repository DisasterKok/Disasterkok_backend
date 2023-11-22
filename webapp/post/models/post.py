from django.db import models

class Post(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=30, null=False)
    content = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    view = models.IntegerField(default=0)
    like = models.IntegerField(default=0)

    class Meta:
        db_table = 'post'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'