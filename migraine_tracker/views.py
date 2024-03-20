from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MigraineAanvalForm
from .models import MigraineAanval, Symptoom, Trigger

def add_migraine_aanval(request):
    if request.method == 'POST':
        form = MigraineAanvalForm(request.POST)
        if form.is_valid():
            nieuwe_aanval = form.save(commit=False)
            nieuwe_aanval.save()  # sla de aanval eerst op

            # Voeg triggers toe aan de aanval
            triggers = form.cleaned_data['triggers']
            for trigger in triggers:
                nieuwe_aanval.triggers.add(trigger)
            
            # Voeg symptomen toe aan de aanval
            symptomen = form.cleaned_data['symptomen']
            for symptoom in symptomen:
                nieuwe_aanval.symptomen.add(symptoom)
            
            return redirect('overzicht')  # redirect naar de overzichtspagina
    else:
        form = MigraineAanvalForm()
   
    return render(request, 'migraine/add_migraine_aanval.html', {'form': form})

def overzicht(request):
    aanvallen = MigraineAanval.objects.all()
    return render(request, 'migraine/overzicht.html', {'aanvallen': aanvallen})
