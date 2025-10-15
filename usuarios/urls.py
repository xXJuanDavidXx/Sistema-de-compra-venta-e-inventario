from django.urls import path
from .views import CrearUsuario, LoginUsuario, logout_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('crear_usuario/', CrearUsuario.as_view(), name='crear_usuario'),
    path('login/', LoginUsuario.as_view(), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='recuperar/restablecer_contraseña.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='recuperar/Done1.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='recuperar/confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='recuperar/complete.html'), name='password_reset_complete'),
    path('logout/', logout_view, name='logout'),
        ]


