from django.urls import path
from . import views

urlpatterns = [
    path('migraine/', views.overzicht, name='overzicht'),  # Overzicht van migraineaanvallen
    path('migraine/Add/', views.add_migraine_aanval, name='add_migraine_aanval'),  # Pagina om een nieuwe migraineaanval toe te voegen
    path('migraine/Delete/<int:aanval_id>/', views.delete_migraine_aanval, name='delete_migraine_aanval'),
]
