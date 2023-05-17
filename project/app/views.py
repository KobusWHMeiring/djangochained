from django.shortcuts import render

# Create your views here.

def home(request, name):
    context = {"userName" : name}
    return(render(request, "app/index.html", context))