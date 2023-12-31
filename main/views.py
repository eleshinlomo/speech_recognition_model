from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import speech_recognition
import pyttsx3


# Create your views here.
def index(request):
    test = 'Welcome to Speech Recognition project by MYAFROS'
    return HttpResponse(test)


def speech_to_text():
    try:
        recognizer = speech_recognition.Recognizer()

        with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio)
                text = text.lower()
        return text
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()

def get_speech_to_text_response():
    try:
        response = speech_to_text()
        return response
    except Exception as e:
        return {"message": str(e)}
        
