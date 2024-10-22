from django.shortcuts import render
from django.views.generic import FormView
from .forms import Crear_Usuario
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


# Create your views here.

class CrearUsuario(FormView):
    template_name = 'signup.html'
    form_class = Crear_Usuario
    success_url = reverse_lazy('login')


class LoginUsuario(LoginView):
    template_name = 'login.html'

