from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
# Create your views here.
 
def index(request):
    return render(request, 'home/home.html')
def contact(request):
    return render(request, 'home/contact.html')
def about(request):
    return render(request, 'home/about.html')