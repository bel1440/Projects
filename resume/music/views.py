from django.shortcuts import render
from .models import Singers, Songs, TypeMusics, Users

def music(request):
    Types = TypeMusics.objects.all()
    Singerss = Singers.objects.all()
    Songss = Songs.objects.all()
    return render(request, 'music/music.html', {'Types': Types, 'Singerss': Singerss, 'Songss': Songss})