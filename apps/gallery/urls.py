from django.urls import path
from apps.gallery.views import index, image, search, add_image

urlpatterns = [
    path('', index, name='index'),
    path('image/<int:photo_id>', image, name='image'),
    path('search', search, name='search'),
    path('add-image', add_image, name='add_image'),
]
