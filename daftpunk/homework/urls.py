from django.urls import path
from . import views

urlpatterns = [
  path("<int:id>/songinsta/", views.song_insta, name="sing_pick"),
  path("<int:id>/songpick/", views.song_pick, name="sing_pick"),
  path("index/", views.index, name="index"),
  path("", views.home, name="home"),
]