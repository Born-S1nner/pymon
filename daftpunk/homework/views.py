from django.shortcuts import render
from django.http import HttpResponse
from .models import Song, SoundBass

# Create your views here.

def index(res, id): 
  s = Song.objects.get(id=id)
  sb = s.soundbass_set.get(id=1)
  return HttpResponse("<h1>%s</h1><br/><h2>%s</h2>" %(s.title, sb.insturment))

def home(res): 
  return HttpResponse("DaftPunk still lives")
