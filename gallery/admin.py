from django.contrib import admin

from gallery.models import Photo

class ListPhotos(admin.ModelAdmin):
    """Customize the display of the Photo model in Django Admin."""

    list_display = ('id', 'title', 'category', 'caption', 'public')
    list_editable = ('public',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category',)
    list_per_page = 10

admin.site.register(
    Photo,
    ListPhotos,
    )
