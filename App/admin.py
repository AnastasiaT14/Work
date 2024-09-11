from django.contrib import admin
from .models import Workout, Exercises, Measurements

admin.site.register(Workout)
admin.site.register(Exercises)
admin.site.register(Measurements)
