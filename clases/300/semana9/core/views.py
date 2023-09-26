from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    titulo = "Home"
    datos ={        
        "titulo":titulo
    }
    return render(request, 'core/index.html',datos)

def carreras(request):
    titulo = "Carreras"
    datos ={        
        "titulo":titulo
    }
    return render(request,'core/carreras.html',datos)

def docentes(request):
    titulo = "Docentes"
    total_docentes = 0



    datos ={        
        "titulo":titulo,
        "total_docentes":total_docentes
    }
    return render(request,'core/docentes.html',datos)