from django.shortcuts import render
from django.http import HttpResponse
from .models import Carrera

def home(request):
    #return HttpResponse("Hola Mundo")
    return render(request,'core/home.html')

def carreras(request):
    titulo = "Carreras"

    # lista_carreras = [
    #     "Técnico Universitario en Informática",
    #     "Ingeniería en Informática",
    #     "Ingeniería de Ejecución en Software",  
    # ]

    lista_carreras = Carrera.objects.all()

    data = {
        "titulo":titulo,
        "lista_carreras":lista_carreras
    }
    return render(request,'core/carreras.html', data)

def docentes(request):

    return render(request,'core/docentes.html')
