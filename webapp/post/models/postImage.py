from django.db import models

def image_upload_path(instance, filename):
    return f'post/{instance.post.id}/{filename}'

class PostImage(models.Model):
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to=image_upload_path, null=False)

    class Meta:
        db_table = 'post_image'
        verbose_name = 'Post_Image'
        verbose_name_plural = 'Post_Images'