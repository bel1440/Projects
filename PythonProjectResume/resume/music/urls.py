from django.urls import path
from . import views

urlpatterns = [
    path('', views.music),
    path('list/', views.list),
    path('genre/', views.genre),
    path('singers/', views.singers),
]