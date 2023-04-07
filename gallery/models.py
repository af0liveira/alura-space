from django.db import models

class Photo(models.Model):
    """Class for representing an photograph in the database."""
    title = models.CharField(max_length=100, null=False, blank=False)
    caption = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    filename = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return f'Photo [title={self.title}]'
