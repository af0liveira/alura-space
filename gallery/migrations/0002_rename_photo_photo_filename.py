# Generated by Django 4.1 on 2023-04-07 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='photo',
            new_name='filename',
        ),
    ]
