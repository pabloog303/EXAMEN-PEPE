from django.urls import path
from . import views

urlpatterns = [
    path('', views.agregar_auto, name='index'),  # Redirige automáticamente a agregar_auto
    path('agregar_auto/', views.agregar_auto, name='agregar_auto'),
    path('lista_autos/', views.lista_autos, name='lista_autos'),
]