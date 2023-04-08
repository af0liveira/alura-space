from django.shortcuts import render, get_object_or_404

from gallery.models import Photo

def index(request):
    photos = Photo.objects.order_by('-date_added').filter(public=True)
    return render(request, 'gallery/index.html', dict(cards=photos))

def image(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    return render(request, 'gallery/image.html', dict(photo=photo))

def search(request):
    return render(request, 'gallery/search.html')