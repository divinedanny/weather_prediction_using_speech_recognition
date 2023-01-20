from cgi import test
from email.mime import audio
from requests import Response
import speech_recognition as sr
from django.shortcuts import render
from .models import WeatherModel, SpeechInput
from .serializers import WeatherPredictionSerializers, SpeechRecognitionSerializers
from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser
import os
import pyttsx3
from django.core.files.storage import default_storage
# Create your views here.
class CurrentWeatherView(generics.CreateAPIView):
    queryset = WeatherModel.objects.order_by("-created")
    serializer_class = WeatherPredictionSerializers
    parser_classes = (MultiPartParser,FormParser)
    
    

    
class SpeechRecognitionView(generics.CreateAPIView):
    queryset = SpeechInput.objects.order_by("-created")
    serializer_class = SpeechRecognitionSerializers
    parser_classes = (MultiPartParser,FormParser)
    
def speech_recognition(request):
    if request.method == 'POST':
        file = request.FILES['voice_url'].file
        default_storage.save('sound.wav', file)
        sound=None
        with default_storage.open('sound.wav') as v:
            recognizer = sr.Recognizer()
            text = recognizer.recognize_google(v)
            text = text.lower()
            print(f"Recognized: {text}")

            # while True:
                # try:
                #     with sr.Microphone() as mic:
                #         recognizer.adjust_for_ambient_noise(mic, duration=0.3)
                #         audio = recognizer.listen(mic)
                #         text = recognizer.recognize_google(audio)
                #         text = text.lower()
                            
                #         print(f"Recognized: {text}")
                # except Exception as e:
                #     print(e)
                #     recognizer = sr.Recognizer()
                #     continue
    return Response(test)

    

# def upload(request):
#     customHeader = request.META['HTTP_MYCUSTOMHEADER']

#     # obviously handle correct naming of the file and place it somewhere like media/uploads/
#     filename = str(SpeechInput.objects.count())
#     filename = filename + "name" + ".wav"
#     uploadedFile = open(filename, "wb")
#     # the actual file is in request.body
#     uploadedFile.write(request.body)
#     uploadedFile.close()
#     # put additional logic like creating a model instance or something like this here
#     r = sr.Recognizer()
#     harvard = sr.AudioFile(filename)
#     with harvard as source:
#         audio = r.record(source)
#     msg = r.recognize_google(audio)
#     os.remove(filename)
#     chat_message = SpeechInput(user=request.user, message=msg)
#     if msg != '':
#         chat_message.save()
#         print(chat_message)
#     return chat_message
    