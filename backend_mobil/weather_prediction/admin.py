from django.contrib import admin
from .models import WeatherModel, SpeechInput

# Register your models here.
admin.site.register(WeatherModel)
admin.site.register(SpeechInput)