from django.http import HttpResponse
from django.shortcuts import render
from .models import job

def home(request):
    jobs=job.objects
    return render(request,'jobs/Home.html',{'jobs':jobs})
