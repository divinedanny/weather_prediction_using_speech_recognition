from django.db import models

# Create your models here.


def Voice(instance, filename):
    return f'voices/{filename}'


def voice_title(filename):
    return filename


class WeatherModel(models.Model):
    humidity = models.IntegerField(null=True)
    windSpeed = models.IntegerField(null=True)
    temperature = models.IntegerField(null=True)
    cloud = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    
def __int__(self):
    return self.temperature
    
class SpeechInput(models.Model):
    voice_content = models.TextField(null=True)
    voice_title = models.CharField(max_length=200)
    file_type = models.CharField(max_length=10)
    voice_url = models.FileField(upload_to=Voice)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.voice_title
