from django.urls import path
from . import views

urlpatterns = [
    path('', views.music, name='music'),
    path('list/', views.list, name='list'),
    path('genre/', views.genre, name='genre'),
    path('singers/', views.singers, name='singer'),
    path('add-music/', views.add_music, name='music'),
    path('<int:pk>', views.MusicDetailView.as_view(), name='music-details')
]