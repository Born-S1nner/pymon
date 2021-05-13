from django.urls import path
from . import views

app_name = "homework"

urlpatterns = [
  path("create/", views.create, name="create"),
  path("songinsta/<int:id>/", views.song_insta, name="sing_insta"),
  path("songpick/<int:id>/", views.song_pick, name="sing_pick"),
  path("index/", views.index, name="index"),
  path("", views.home, name="home"),
]