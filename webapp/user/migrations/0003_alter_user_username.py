# Generated by Django 4.2.3 on 2023-11-18 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_googleid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=40, unique=True, verbose_name='유저 아이디'),
        ),
    ]
