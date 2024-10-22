from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Crear_Usuario(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

