# Generated by Django 4.2.3 on 2024-02-15 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
