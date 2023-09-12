from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    title="Área Informática SVM"
    menu= "<ul>"
    menu+= '<li><a href="">Inicio</a></li>'
    menu+= '<li><a href="carreras/">Carreras</a></li>'
    menu+= '<li><a href="docentes/">Docentes</a></li>'
    menu+="</ul>"

    page = "<html>"
    page+= "<head>"
    page+="<title>"+title+"</title>"
    page+= "</head>"
    page+= "<body>"
    page+="<h1>"+title+"</h1>"
    page+="<br>"+menu
    page+= "</body>"
    page+= "</html>"
    return HttpResponse(page)

def carreras(request):
    title ="Carreras"
    page = "<html>"
    page+= "<head>"
    page+="<title>"+title+"</title>"
    page+= "</head>"
    page+= "<body>"
    page+="<h1>"+title+"</h1>"
    page+= "</body>"
    page+= "</html>"
    return HttpResponse(page)

def docentes(request):
    title ="Docentes"
    page = "<html>"
    page+= "<head>"
    page+="<title>"+title+"</title>"
    page+= "</head>"
    page+= "<body>"
    page+="<h1>"+title+"</h1>"
    page+= "</body>"
    page+= "</html>"
    return HttpResponse(page)