# admin.py
from django.contrib import admin
from .models import MigraineAanval, Symptoom, Trigger

admin.site.register(MigraineAanval)
admin.site.register(Symptoom)
admin.site.register(Trigger)
