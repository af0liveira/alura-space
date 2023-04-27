from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# from datetime import datetime

class Photo(models.Model):
    """Class for representing an photograph in the database."""

    CATEGORIES = [
        ('', '---'),
        ('ESTRELA', 'Estrela'),
        ('GALAXIA', 'Galáxia'),
        ('NEBULOSA', 'Nebulosa'),
        ('PLANETA', 'Planeta'),
    ]

    title = models.CharField(max_length=100, null=False, blank=False)
    caption = models.CharField(max_length=250, null=False, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORIES, default='')
    description = models.TextField(null=False, blank=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    public = models.BooleanField(default=True)
    date_added = models.DateTimeField(default=timezone.now, blank=False)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user',
    )

    def __str__(self):
        return f'Photo [title={self.title}]'
