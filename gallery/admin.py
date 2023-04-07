from django.contrib import admin

from gallery.models import Photo

class ListPhotos(admin.ModelAdmin):
    """Customize the display of the Photo model in Django Admin."""

    list_display = ('id', 'title', 'caption')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(
    Photo,
    ListPhotos,
    )
