# Generated by Django 4.1 on 2023-04-07 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_rename_photo_photo_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='category',
            field=models.CharField(choices=[('', '---'), ('ESTRELA', 'Estrela'), ('GALAXIA', 'Galáxia'), ('NEBULOSA', 'Nebulosa'), ('PLANETA', 'Planeta')], default='', max_length=100),
        ),
    ]