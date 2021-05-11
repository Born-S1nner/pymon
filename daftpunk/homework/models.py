from django.db import models

# Create your models here.
class Song(models.Model):
  title = models.CharField(max_length=200)
  composer = models.CharField(max_length=200)
  likes = models.IntegerField(default=0)

  def __str__(self):
    return self.title, self.composer

class SoundBass(models.Model):
  song = models.ForeignKey(Song, on_delete=models.CASCADE)
  insturment = models.CharField(max_length=300)
  
  def __str__(self):
    return self.insturment

