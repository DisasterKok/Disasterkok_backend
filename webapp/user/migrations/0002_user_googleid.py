# Generated by Django 4.2.3 on 2023-11-11 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='googleID',
            field=models.CharField(blank=True, max_length=225, null=True, unique=True, verbose_name='구글 아이디'),
        ),
    ]