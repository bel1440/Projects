from django.contrib import admin
from .models import Singers, Songs, TypeMusics, Users

admin.site.register(Singers)
admin.site.register(Songs)
admin.site.register(TypeMusics)
admin.site.register(Users)