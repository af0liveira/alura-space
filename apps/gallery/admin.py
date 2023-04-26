from django.contrib import admin

from apps.gallery.models import Photo

class ListPhotos(admin.ModelAdmin):
    """Customize the display of the Photo model in Django Admin."""

    list_display = ('id', 'title', 'category', 'caption', 'date_added', 'public')
    list_editable = ('public',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category','user')
    list_per_page = 10

admin.site.register(
    Photo,
    ListPhotos,
    )
