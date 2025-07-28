from .models import Singers, Songs, TypeMusics
from django.forms import ModelForm, TextInput, FileInput, ClearableFileInput

class SongsForm(ModelForm):
    class Meta:
        model = Songs
        fields = ['name_song', 'file', 'img_song']

        widgets = {
            'name_song': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название песни'
            }),
            'file': FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'путь к песне'
            }),
            'img_song': FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'загрузите фото'
            })
        }

class SingersForm(ModelForm):
    class Meta:
        model = Singers
        fields = ['name_singer', 'description', 'img_singer']

        widgets = {
            'name_singer': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'имя исполнителя'
            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'описание жанра'
            }),
            'img_singer': FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'загрузите фото'
            })
        }

class TypeMusicsForm(ModelForm):
    class Meta:
        model = TypeMusics
        fields = ['name_type', 'description', 'img_type']

        widgets = {
            'name_type': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название жанра'
            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'описание жанра'
            }),
            'img_type': FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'загрузите фото'
            })
        }