from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Song, SoundBass
from .forms import CreateNewSong

# Create your views here.

def index(res): 
  sl = Song.objects.all()
  return render(res, "homework/songlist.html", {"sl": sl})

def song_pick(res, id):
  s = Song.objects.get(id=id)
  template = """
  <link rel='stylesheet' type='text/css' href='http://127.0.0.1:8000/static/homework/style.css' />
  <div class='content'>
    <h1>%s</h1>
    <br/>
    <h2>By: %s</h2>
    <hr/>
    <a href='/songinsta/%s/'>details</a>
    <br/>
    <a href='/index/'>back</a>
  <div>
  """ %(s.title, s.composer, s.id)
  return HttpResponse(template)

def song_insta(res, id):
  sb = SoundBass.objects.get(id=id)
  template = """
  <link rel='stylesheet' type='text/css' href='http://127.0.0.1:8000/static/homework/style.css' />
  <div class='content'>
    <p>Insturment: %s</p>
    <p>Tempo: %s</p>
    <hr/>
    <a href='/songpick/%s/'>back</a>
  </div>
  """ %(sb.insturment, sb.tempo, sb.id)
  return HttpResponse(template)

def create(res):
  if res.method == "POST":
    form = CreateNewSong(res.POST)
    if form.is_valid():
      CT = form.cleaned_data["title"]
      CC = form.cleaned_data["composer"]
      ns = Song(title=CT, composer=CC)
      ns.save()
    return HttpResponseRedirect("/songpick/%i" %ns.id)
  else:
    form = CreateNewSong()
  return render(res, "homework/create.html", {"form":form})

def home(res): 
  return render(res, "homework/home.html", {})