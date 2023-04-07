from django.db import models

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
    filename = models.CharField(max_length=150, null=False, blank=False)
    public = models.BooleanField(default=False)

    def __str__(self):
        return f'Photo [title={self.title}]'
