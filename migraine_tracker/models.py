# models.py

from django.db import models

class Symptoom(models.Model):
    naam = models.CharField(max_length=100)

    def __str__(self):
        return self.naam

class Trigger(models.Model):
    naam = models.CharField(max_length=100)

    def __str__(self):
        return self.naam

class MigraineAanval(models.Model):
    datum = models.DateField()
    pijn_score = models.IntegerField()
    symptomen = models.ManyToManyField(Symptoom, related_name='migraine_aanvallen')
    triggers = models.ManyToManyField(Trigger, related_name='migraine_aanvallen')
    notities = models.TextField(blank=True, null=True)
