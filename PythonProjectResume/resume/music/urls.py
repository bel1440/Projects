from django.urls import path
from . import views

urlpatterns = [
    path('', views.music, name='music'),
    path('list/', views.list, name='list'),
    path('genre/', views.genre, name='genre'),
    path('singers/', views.singers, name='singer'),
    path('add-music/', views.add_music, name='music'),
    path('list/<int:pk>', views.MusicDetailView.as_view(), name='music-details'),
    path('add-singers/', views.add_singer, name='singer'),
    path('singers/<int:pk>', views.SingerDetailView.as_view(), name='singer-details'),
    path('add-genre/', views.add_genre, name='genre'),
    path('genre/<int:pk>', views.GenreDetailView.as_view(), name='genre-details')
]