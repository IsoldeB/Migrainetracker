from django import forms
from .models import MigraineAanval, Symptoom, Trigger

class MigraineAanvalForm(forms.ModelForm):
    symptomen = forms.ModelMultipleChoiceField(queryset=Symptoom.objects.all(), widget=forms.CheckboxSelectMultiple)
    triggers = forms.ModelMultipleChoiceField(queryset=Trigger.objects.all(), widget=forms.CheckboxSelectMultiple)
    
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['symptomen'].queryset = Symptoom.objects.all()
        self.fields['triggers'].queryset = Trigger.objects.all()
        self.fields['symptomen'].widget.attrs.update({'aria-labelledby': 'symptomen-label'})
        self.fields['triggers'].widget.attrs.update({'aria-labelledby': 'triggers-label'})
        self.fields['notities'].widget.attrs.update({'aria-describedby': 'notities-help-text'})

    def as_accessible(self):
        """
        Renders the form in an accessible way, suitable for screen readers.
        """
        output = ''
        for field in self:
            output += str(field) + '<br>'
            if field.errors:
                for error in field.errors:
                    output += '<span role="alert">{}</span><br>'.format(error)
        return output
