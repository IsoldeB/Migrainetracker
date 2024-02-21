from django.db import models

class MigraineAanval(models.Model):
    datum = models.DateField()
    pijn_score = models.IntegerField()
    symptomen = models.ManyToManyField('Symptoom', related_name='migraine_aanvallen')
    triggers = models.ManyToManyField('Trigger', related_name='migraine_aanvallen')
    notities = models.TextField(blank=True, null=True)  # Nieuw veld voor extra notities

class Symptoom(models.Model):
    SYMPTOOM_CHOICES = (
        ('Hoofdpijn', 'Hoofdpijn'),
        ('Misselijkheid', 'Misselijkheid'),
        ('Duizeligheid', 'Duizeligheid'),
        # Voeg hier meer symptomen toe indien nodig
    )
    naam = models.CharField(max_length=100, choices=SYMPTOOM_CHOICES)

class Trigger(models.Model):
    TRIGGER_CHOICES = (
        ('Stress', 'Stress'),
        ('Cafeïne', 'Cafeïne'),
        ('Veranderingen in het weer', 'Veranderingen in het weer'),
        # Voeg hier meer triggers toe indien nodig
    )
    naam = models.CharField(max_length=100, choices=TRIGGER_CHOICES)
