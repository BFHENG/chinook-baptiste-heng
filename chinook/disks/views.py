from django.shortcuts import render, get_object_or_404
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
    
def detail_album (request, album_id):
    #return HttpResponse("You're looking at album %s." % album_id)
    
    album = get_object_or_404(Album, pk=album_id)
    
    return render(request, 'disks/album_detail.html', {'album': album})

    
# Create your views here.
