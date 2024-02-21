from django.test import TestCase
from .models import MigraineAanval, Symptoom, Trigger
from datetime import date

class ModelTests(TestCase):
    def setUp(self):
        # Maak enkele symptomen aan voor gebruik in tests
        self.symptoom1 = Symptoom.objects.create(naam='Hoofdpijn')
        self.symptoom2 = Symptoom.objects.create(naam='Misselijkheid')
        self.symptoom3 = Symptoom.objects.create(naam='Duizeligheid')

        # Maak enkele triggers aan voor gebruik in tests
        self.trigger1 = Trigger.objects.create(naam='Stress')
        self.trigger2 = Trigger.objects.create(naam='Cafeïne')
        self.trigger3 = Trigger.objects.create(naam='Veranderingen in het weer')

    def test_migraine_aanval_aanmaken(self):
        # Maak een migraineaanval aan
        aanval = MigraineAanval.objects.create(
            datum=date.today(),
            pijn_score=7
        )
        # Voeg symptomen en triggers toe aan de aanval
        aanval.symptomen.add(self.symptoom1)
        aanval.triggers.add(self.trigger1)

        # Controleer of de aanval is aangemaakt en de relaties correct zijn ingesteld
        self.assertEqual(MigraineAanval.objects.count(), 1)
        self.assertEqual(aanval.symptomen.count(), 1)
        self.assertEqual(aanval.triggers.count(), 1)

    def test_symptoom_en_trigger_aanmaken(self):
        # Controleer of symptomen en triggers correct zijn aangemaakt
        self.assertEqual(Symptoom.objects.count(), 3)
        self.assertEqual(Trigger.objects.count(), 3)
