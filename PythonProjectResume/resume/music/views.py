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
