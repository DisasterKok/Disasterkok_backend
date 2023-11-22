from django.db import models
from post.models import Post

def image_upload_path(instance, filename):
    return f'media/posts/{instance.post.id}/{filename}/%Y/%m/%d'

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='image')
    image = models.FileField(upload_to=image_upload_path, null=False)

    def __int__(self):
        return self.id

    class Meta:
        db_table = 'post_image'
        verbose_name = 'Post_Image'
        verbose_name_plural = 'Post_Images'