from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello this is the index")


def specific(request, conversation_id):
    response = "you are asking for the following id: %s"
    return HttpResponse(response % conversation_id)
    