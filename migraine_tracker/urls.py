from django.urls import path
from . import views

urlpatterns = [
    path('', views.migraine_overzicht, name='migraine_overzicht'),  # Overzicht van migraineaanvallen
    path('Add/', views.add_migraine_aanval, name='add_migraine_aanval'),  # Pagina om een nieuwe migraineaanval toe te voegen
]