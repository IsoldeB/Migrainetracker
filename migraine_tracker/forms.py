from django import forms
from .models import MigraineAanval, Symptoom, Trigger

class MigraineAanvalForm(forms.ModelForm):
    symptomen = forms.ModelMultipleChoiceField(queryset=Symptoom.objects.all(), widget=forms.CheckboxSelectMultiple)
    triggers = forms.ModelMultipleChoiceField(queryset=Trigger.objects.all(), widget=forms.CheckboxSelectMultiple)
    pijn_score = forms.IntegerField(min_value=0, max_value=10)

    class Meta:
        model = MigraineAanval
        fields = ['datum', 'pijn_score', 'symptomen', 'triggers', 'notities']
        labels = {
            'datum': 'Datum',
            'pijn_score': 'Pijnscore',
            'symptomen': 'Symptomen',
            'triggers': 'Triggers',
            'notities': 'Notities (optioneel)',
        }
        widgets = {
            'datum': forms.DateInput(attrs={'id': 'id_datum', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['symptomen'].widget.attrs.update({'aria-labelledby': 'symptomen-label'})
        self.fields['triggers'].widget.attrs.update({'aria-labelledby': 'triggers-label'})
        self.fields['notities'].widget.attrs.update({'aria-describedby': 'notities-help-text'})

    def clean(self):
        cleaned_data = super().clean()
        symptomen = cleaned_data.get('symptomen')
        triggers = cleaned_data.get('triggers')
        if not symptomen:
            self.add_error('symptomen', 'Selecteer minstens één symptoom.')
        if not triggers:
            self.add_error('triggers', 'Selecteer minstens één trigger.')
        return cleaned_data

    def clean_pijn_score(self):
        pijn_score = self.cleaned_data['pijn_score']
        if pijn_score < 0 or pijn_score > 10:
            raise forms.ValidationError("Pijnscore moet tussen 0 en 10 liggen.")
        return pijn_score

    def save(self, commit=True):
        migraine_aanval = super().save(commit=False)
        if commit:
            migraine_aanval.save()
            self.save_m2m()  # Save the many-to-many relationships after saving the instance
        return migraine_aanval
