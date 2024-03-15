from django.urls import path
from migraine_tracker import views

urlpatterns = [
    path('', views.migraine_overzicht, name='home'),  # Dit is het patroon voor de hoofdpagina
    path('migraine/', views.migraine_overzicht, name='migraine_overzicht'),
    # Andere URL-patronen hier...
]
