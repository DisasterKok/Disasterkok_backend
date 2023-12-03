from django.db import models

from user.models import User

class Notification(models.Model):
    class Meta:
        db_table = 'notification'
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

