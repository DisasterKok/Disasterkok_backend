from django.db import models

from notification.models import Notification


ALIASTYPE_CATEGORY_CHOICES = (
    ('home', 'home'),
    ('school', 'school'),
    ('work', 'work'),
    ('etc', 'etc'),
)
class Region(models.Model):
    class Meta:
        db_table = 'region'
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    notification = models.ForeignKey(
        Notification,
        on_delete=models.CASCADE,
    )

    default = models.BooleanField(
        default=False,
    )

    onOff = models.BooleanField(
        default=True,
        null=False,
    )

    name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    address = models.TextField(
        null=False,
    )

    roadAdress = models.CharField(
        null=False,
    )

    zoneCode = models.CharField(
        null=False,
    )

    aliasType = models.CharField(
        choices=ALIASTYPE_CATEGORY_CHOICES,
        null=False,
    )