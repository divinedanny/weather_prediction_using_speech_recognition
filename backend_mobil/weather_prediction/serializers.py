from dataclasses import field
from .models import WeatherModel, SpeechInput
from django.contrib.auth.models import User
from rest_framework import serializers

class WeatherPredictionSerializers(serializers.ModelSerializer):
    class Meta:
        model = WeatherModel
        fields = ['id','temperature','windSpeed','cloud','humidity']
        
class SpeechRecognitionSerializers(serializers.ModelSerializer):
    class Meta:
        model = SpeechInput
        fields = ['voice_title', 'voice_url']