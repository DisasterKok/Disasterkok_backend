from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'tag'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name

