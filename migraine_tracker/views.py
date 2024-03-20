from django.shortcuts import render, redirect, get_object_or_404
from .forms import MigraineAanvalForm
from .models import MigraineAanval

def add_migraine_aanval(request):
    if request.method == 'POST':
        form = MigraineAanvalForm(request.POST)
        if form.is_valid():
            nieuwe_aanval = form.save(commit=False)

            # Eerst de aanval opslaan om een ID toe te wijzen
            nieuwe_aanval.save()

            # Voeg triggers toe aan de aanval
            triggers = form.cleaned_data['triggers']
            nieuwe_aanval.triggers.set(triggers)

            # Voeg symptomen toe aan de aanval
            symptomen = form.cleaned_data['symptomen']
            nieuwe_aanval.symptomen.set(symptomen)

            # Haal medicijnen op uit het POST-verzoek
            medicijnen = request.POST.get('medicijnen', '')

            # Sla de aanval op met de medicijnen als een string
            nieuwe_aanval.medicijnen = medicijnen

            # Sla de aanval opnieuw op met de medicijnen als een string
            nieuwe_aanval.save()
            
            return redirect('overzicht')  # Redirect naar de overzichtspagina
    else:
        form = MigraineAanvalForm()
   
    return render(request, 'migraine/add_migraine_aanval.html', {'form': form})

def overzicht(request):
    aanvallen = MigraineAanval.objects.all()
    return render(request, 'migraine/overzicht.html', {'aanvallen': aanvallen})

def delete_migraine_aanval(request, aanval_id):
    # Haal de migraineaanval op uit de database
    aanval = get_object_or_404(MigraineAanval, pk=aanval_id)
    
    if request.method == 'POST':
        # Als het een POST-verzoek is, verwijder de aanval
        aanval.delete()
        # Redirect naar het overzichtspagina na verwijdering
        return redirect('overzicht')
    
    # Render het bevestigingsvenster voor het verwijderen van de aanval
    return render(request, 'migraine/delete_migraine_aanval.html', {'aanval': aanval})
