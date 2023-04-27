from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from apps.gallery.models import Photo
from apps.gallery.forms import PhotoForm

def index(request):
    photos = Photo.objects.order_by('-date_added').filter(public=True)
    return render(request, 'gallery/index.html', dict(cards=photos))

def image(request, photo_id):
    if not request.user.is_authenticated:
        messages.error(request, "Faça seu login para prosseguir!")
        return redirect('login')

    photo = get_object_or_404(Photo, pk=photo_id)
    return render(request, 'gallery/image.html', dict(photo=photo))

def search(request):
    if not request.user.is_authenticated:
        messages.error(request, "Faça seu login para prosseguir!")
        return redirect('login')

    photos = Photo.objects.order_by('-date_added').filter(public=True)

    if 'search' in request.GET:
        search_key = request.GET['search']
        if search_key:
            photos = photos.filter(title__contains=search_key)

    return render(request, 'gallery/search.html', dict(cards=photos, search_key=search_key))

def add_image(request):
    if not request.user.is_authenticated:
        messages.error(request, "Faça seu login para prosseguir!")
        return redirect('login')

    form = PhotoForm

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            title = form['title'].value()
            form.save()
            messages.success(request, f"Foto cadastrada: '{title}'.")
            return redirect('index')

    return render(request, 'gallery/add_image.html', dict(form=form))

def edit_image(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    form = PhotoForm(instance=photo)

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)

        if form.is_valid():
            title = form['title'].value()
            form.save()
            messages.success(request, f"Foto modificada: '{title}'.")
            return redirect('index')

    return render(request, 'gallery/edit_image.html', dict(form=form,
                  photo_id=photo_id))

def delete_image(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    title = photo.title
    photo.delete()
    messages.success(request, f"Foto removida: '{title}'.")
    return redirect('index')

def filter(request, category):
    if not request.user.is_authenticated:
        messages.error(request, "Faça seu login para prosseguir!")
        return redirect('login')

    photos = Photo.objects.order_by('-date_added')\
                          .filter(public=True, category=category)

    return render(request, 'gallery/index.html', dict(cards=photos))