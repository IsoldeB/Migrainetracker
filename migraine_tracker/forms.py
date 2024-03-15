from django import forms
from .models import MigraineAanval

class MigraineAanvalForm(forms.ModelForm):
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
        self.fields['symptomen'].widget.attrs['aria-describedby'] = 'symptomen-help-text'
        self.fields['triggers'].widget.attrs['aria-describedby'] = 'triggers-help-text'
        self.fields['notities'].widget.attrs['aria-describedby'] = 'notities-help-text'

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
