from django.shortcuts import render

from gallery.models import Photo

def index(request):
    photos = Photo.objects.all()
    return render(request, 'gallery/index.html', dict(cards=photos))

def image(request):
    return render(request, 'gallery/image.html')
