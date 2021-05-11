from django.shortcuts import render
from django.http import HttpResponse
from .models import Song, SoundBass

# Create your views here.

def index(res, id): 
  s = Song.objects.get(id=id)
  return HttpResponse("%s" % s.title)

def home(res): 
  return HttpResponse("DaftPunk still lives")
