from django.shortcuts import render

def index(request):

    data = {
        1: {
            'name': 'Nebulosa de Carina',
            'description': 'webbtelescope.org / NASA / James Webb',
        },
        2: {
            'name': 'Galáxia NGC 1079',
            'description': 'nasa.org / NASA / Hubble',
        }
    }

    return render(request, 'gallery/index.html', dict(cards=data))

def image(request):
    return render(request, 'gallery/image.html')
