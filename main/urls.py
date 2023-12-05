from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('speech_to_text/', views.get_speech_to_text_response, name='speech to text'),
]