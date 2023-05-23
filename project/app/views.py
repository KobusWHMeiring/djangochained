from django.shortcuts import render, HttpResponse
from .models import Conversation, Users, Tools
# Create your views here.

def home(request):
    tools = Tools.objects.all()
    
    context = {"tools": tools}
    return(render(request, "app/index.html", context))

def choose(request):
    content = "You've been navigated!  Still figuring out how to pass the info"
    
   
    
    return HttpResponse(content)