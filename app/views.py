from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def jampandu(request):
    return HttpResponse('<h1><marquee>hai jampandu how are u </h1></marquee>')
def jigelrani(request):
    return HttpResponse('<h1><marquee>hai rani how are u </h1></marquee>')
