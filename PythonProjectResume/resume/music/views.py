from django.shortcuts import render, redirect
from .models import Singers, Songs, TypeMusics, Users
from .forms import SongsForm, SingersForm, TypeMusicsForm
from django.views.generic import DetailView

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

def add_music(request):
    error = ''
    if request.method == 'POST':
        form_music = SongsForm(request.POST)
        if form_music.is_valid():
            form_music.save()
            return redirect('music')
        else:
            error = 'Ошибка в заполнении данных'

    form_music = SongsForm()

    data = {
        'form_music': form_music,
        'error': error
    }
    return render(request, 'music/add-music.html', data)

class MusicDetailView(DetailView):
    model = Songs
    template_name = 'music/musicdetailviews.html'
    context_object_name = 'songs'

def add_singer(request):
    error = ''
    if request.method == 'POST':
        form_singer = SingersForm(request.POST)
        if form_singer.is_valid():
            form_singer.save()
            return redirect('singer')
        else:
            error = 'Ошибка в заполнении данных'

    form_singer = SingersForm()

    data = {
        'form_singer': form_singer,
        'error': error
    }
    return render(request, 'music/add-singers.html', data)

class SingerDetailView(DetailView):
    model = Singers
    template_name = 'music/singerdetailviews.html'
    context_object_name = 'singers'

def add_genre(request):
    error = ''
    if request.method == 'POST':
        form_genre = TypeMusicsForm(request.POST)
        if form_genre.is_valid():
            form_genre.save()
            return redirect('genre')
        else:
            error = 'Ошибка в заполнении данных'

    form_genre = TypeMusicsForm()

    data = {
        'form_genre': form_genre,
        'error': error
    }
    return render(request, 'music/add-genre.html', data)

class GenreDetailView(DetailView):
    model = TypeMusics
    template_name = 'music/genredetailviews.html'
    context_object_name = 'genre'

