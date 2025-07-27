from django.urls import path
from . import views

urlpatterns = [
    path('', views.music, name='music'),
    path('list/', views.list, name='list'),
    path('genre/', views.genre, name='genre'),
    path('singers/', views.singers, name='singer'),
    path('add-music/', views.add_music, name='music-add'),
    path('list/<int:pk>', views.MusicDetailView.as_view(), name='music-details'),
    path('add-singers/', views.add_singer, name='singer-add'),
    path('singers/<int:pk>', views.SingerDetailView.as_view(), name='singer-details'),
    path('add-genre/', views.add_genre, name='genre-add'),
    path('genre/<int:pk>', views.GenreDetailView.as_view(), name='genre-details'),
    path('list/<int:pk>/update', views.MusicUpdateView.as_view(), name='music-update'),
    path('list/<int:pk>/delete', views.MusicDeleteView.as_view(), name='music-delete'),
    path('singers/<int:pk>/update', views.SingerUpdateView.as_view(), name='singer-update'),
    path('singers/<int:pk>/delete', views.SingerDeleteView.as_view(), name='singer-delete'),
    path('genre/<int:pk>/update', views.GenreUpdateView.as_view(), name='genre-update'),
    path('genre/<int:pk>/delete', views.GenreDeleteView.as_view(), name='genre-delete'),
]