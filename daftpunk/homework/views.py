from django.shortcuts import render
from django.http import HttpResponse
from .models import Song, SoundBass

# Create your views here.

def index(res): 
  song_list = Song.objects.all()
  output = ' <br/>'.join([s.title for s in song_list])
  return HttpResponse(output)

def song_pick(res, id):
  s = Song.objects.get(id=id)
  return HttpResponse("<h1>%s</h1><br/><h2>By: %s</h2><hr/>" %(s.title, s.composer))

def song_insta(res, id):
  sb = SoundBass.objects.get(id=id)
  return HttpResponse("<p>Composer: %s</p><p>Tempo: %s</p>" %(sb.insturment, sb.tempo))

def home(res): 
  return HttpResponse("DaftPunk still lives")
