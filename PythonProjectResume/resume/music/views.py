from django.shortcuts import render
from .models import Singers, Songs, TypeMusics, Users

def music(request):
    Types = TypeMusics.objects.all()
    Singerss = Singers.objects.all()
    Songss = Songs.objects.all()
    return render(request, 'music/music.html', {'Types': Types, 'Singerss': Singerss, 'Songss': Songss})

def list(request):
    Songss = Songs.objects.all()
    return render(request, 'music/music-list.html', {'Songss': Songss})

def genre(request):
    Types = TypeMusics.objects.all()
    return render(request, 'music/genre-list.html', {'Types': Types})

def singers(request):
    Singerss = Singers.objects.all()
    return render(request, 'music/singers-list.html', {'Singerss': Singerss})