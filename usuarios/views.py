from django.shortcuts import render
from django.views.generic import FormView
from .forms import Crear_Usuario
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect



# Create your views here.

class CrearUsuario(FormView):
    template_name = 'signup.html'
    form_class = Crear_Usuario
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'registrarse'
        return context


class LoginUsuario(LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context


def logout_view(request):
    logout(request)
    return redirect('login')