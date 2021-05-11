from django.db import models

# Create your models here.
class SoundBass(models.Model):
  insturment = models.CharField(max_length=300)
  
  def __str__(self):
    return self.insturment

class Song(models.Model):
  soundbass = models.ForeignKey(SoundBass, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  likes = models.IntegerField(default=0)

  def __str__(self):
    return self.title

