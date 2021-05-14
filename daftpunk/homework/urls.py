from django.urls import path
from . import views

app_name = "homework"

urlpatterns = [
  path("create/", views.create, name="create"),
  path("", views.home, name="home"),
  path("index/", views.index, name="index"),
  path("songpick/<int:id>/", views.song_pick, name="songpick"),
  path("songinsta/<int:id>/", views.song_insta, name="sing_insta")
]