from django.urls import path
from .views import CurrentWeatherView, SpeechRecognitionView

urlpatterns = [
    path("",CurrentWeatherView.as_view(), name="current"),
    path("voice/", SpeechRecognitionView.as_view(), name="voice"),
]
