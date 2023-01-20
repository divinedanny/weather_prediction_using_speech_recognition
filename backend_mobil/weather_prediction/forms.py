from dataclasses import field
from django.forms import ModelForm
from .models import SpeechInput



class Voiceform(ModelForm):
    class Meta:
        model = SpeechInput
        fields = ['voice_url']