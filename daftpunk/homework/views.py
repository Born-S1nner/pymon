from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(res): 
  return HttpResponse("Around the World")

def home(res): 
  return HttpResponse("DaftPunk still lives")
