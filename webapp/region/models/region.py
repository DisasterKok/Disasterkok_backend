from django.db import models

from notification.models import Notification


class Region(models.Model):
    class Meta:
        db_table = 'region'
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    notification = models.ForeignKey(
        Notification,
        on_delete=models.CASCADE,
    )

    onOff = models.BooleanField(
        default=True,
        null=False,
    )

    nickname = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    address = models.TextField(
        null=False,
    )
