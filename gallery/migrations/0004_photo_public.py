# Generated by Django 4.1 on 2023-04-07 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_photo_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
