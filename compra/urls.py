from django.urls import path
from .views import compra

urlpatterns = [
    path('', compra, name="Compra")
        ]

