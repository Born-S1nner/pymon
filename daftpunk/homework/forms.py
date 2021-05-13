from django import forms

class CreateNewSong(forms.Form):
  title = forms.CharField(label="title", max_length=300)
  composer = forms.CharField(label="composer", max_length=200)
