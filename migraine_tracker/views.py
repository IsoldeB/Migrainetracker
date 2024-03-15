from django.shortcuts import render
from .models import MigraineAanval

def migraine_overzicht(request):
    aanvallen = MigraineAanval.objects.all()
    return render(request, 'migraine/overzicht.html', {'aanvallen': aanvallen})

