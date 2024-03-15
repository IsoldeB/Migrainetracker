from django.shortcuts import render, redirect
from .models import MigraineAanval
from .forms import MigraineAanvalForm

def migraine_overzicht(request):
    aanvallen = MigraineAanval.objects.all()
    return render(request, 'migraine/overzicht.html', {'aanvallen': aanvallen})

def add_migraine_aanval(request):
    if request.method == 'POST':
        form = MigraineAanvalForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect naar een andere pagina of toon een succesbericht
            return redirect('migraine_overzicht')  # Of waar je ook naartoe wilt na het toevoegen
    else:
        form = MigraineAanvalForm()
    return render(request, 'migraine/add_migraine_aanval.html', {'form': form})
