from .models import Singers, Songs, TypeMusics, Users
from django.forms import ModelForm, TextInput

class SongsForm(ModelForm):
    class Meta:
        model = Songs
        fields = ['name_song']

        widgets = {
            'name_song': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название песни'
            })
        }

class SingersForm(ModelForm):
    class Meta:
        model = Singers
        fields = ['name_singer']

class TypeMusicsForm(ModelForm):
    class Meta:
        model = TypeMusics
        fields = ['name_type', 'description']