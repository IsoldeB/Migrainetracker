from django.contrib import admin
from django.urls import path, include
from migraine_tracker import views  # Importeer de views-module van je app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.overzicht, name='home'),  # Overzichtspagina van migraineaanvallen wordt de hoofdpagina
    path('', include('migraine_tracker.urls')),  # Verwijzing naar URL-configuratie van de 'migraine_tracker' app    path('migraine/', views.migraine_overzicht, name='migraine_overzicht'),  # Overzicht van migraineaanvallen

    # Andere URL-patronen hier...
]