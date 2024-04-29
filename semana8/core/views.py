from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("Hola Mundo")
    return render(request,'core/home.html')

def carreras(request):
   
    return render(request,'core/carreras.html')

def docentes(request):

    return render(request,'core/docentes.html')
