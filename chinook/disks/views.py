from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Album


def index(request):
    list_album = Album.objects.all()
    template = loader.get_template('disks/index.html')
    context = {
        'list_album': list_album,
    }
    
    return HttpResponse(template.render(context, request))
    

# Create your views here.
