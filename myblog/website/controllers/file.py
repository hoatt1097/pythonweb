from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import calendar
import time
# Create your views here.
from website.forms import UploadFileForm

def index(request):
    forms = UploadFileForm() 
    return render(request, 'home/trail.html', {'form':forms})

def submit(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload(request.FILES['file'])
            return HttpResponse("<h2>File uploaded successful!</h2>")
        else:
            return HttpResponse("<h2>File uploaded not successful!</h2>")
    
def upload(f): 
    file = open(f.name, 'wb+') 
    for chunk in f.chunks():
        file.write(chunk)

def lich(request):
    forms = UploadFileForm() 
    lich = calendar.month(2018,7)
    localtime = time.asctime(time.localtime(time.time()))
    return render(request,'home/trail.html',{'lich':lich, 'form':forms, 'time':localtime})