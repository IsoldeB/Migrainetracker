from django.db import models

class MigraineAanval(models.Model):
    datum = models.DateField()
    pijn_score = models.IntegerField()
    symptomen = models.ManyToManyField('Symptoom', related_name='migraine_aanvallen')
    triggers = models.ManyToManyField('Trigger', related_name='migraine_aanvallen')
    notities = models.TextField(blank=True, null=True)
    medicaties = models.ManyToManyField('Medicatie', related_name='migraine_aanvallen')

class Symptoom(models.Model):
    SYMPTOOM_CHOICES = (
        ('Hoofdpijn', 'Hoofdpijn'),
        ('Misselijkheid', 'Misselijkheid'),
        ('Duizeligheid', 'Duizeligheid'),
        # Voeg hier meer symptomen toe indien nodig
    )
    naam = models.CharField(max_length=100, choices=SYMPTOOM_CHOICES)

    def __str__(self):
        return self.naam

class Trigger(models.Model):
    TRIGGER_CHOICES = (
        ('Stress', 'Stress'),
        ('Cafeïne', 'Cafeïne'),
        ('Veranderingen in het weer', 'Veranderingen in het weer'),
        # Voeg hier meer triggers toe indien nodig
    )
    naam = models.CharField(max_length=100, choices=TRIGGER_CHOICES)

    def __str__(self):
        return self.naam

class Medicatie(models.Model):
    naam = models.CharField(max_length=100)

    def __str__(self):
        return self.naam
