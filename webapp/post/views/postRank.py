import datetime

from django.utils import timezone

from post.models import Post


def PostRank():
    post = Post.objects.all()
    post = post.order_by('-created_at')
    current_time = timezone.now()
    twenty_four_hours_ago = current_time - timezone.timedelta(hours=24)
    posts = post.filter(created_at__gte=twenty_four_hours_ago)
    posts = posts.order_by('view')
    return posts[:10]
