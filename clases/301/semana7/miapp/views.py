from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    title = "Inicio"
    page = "<html>"
    page+= "<head>"
    page+= "<title>"+title+"</title>"
    page+= "</head>"
    page+= "<body>"
    page+= "<h1>"+title+"</h1>"
    page+= "</body>"
    page+= "<html>"

    return HttpResponse(page)

def vista2(request):
    title = "Vista 2"
    page = "<html>"
    page+= "<head>"
    page+= "<title>"+title+"</title>"
    page+= "</head>"
    page+= "<body>"
    page+= "<h1>"+title+"</h1>"
    page+= "</body>"
    page+= "<html>"

    return HttpResponse(page)