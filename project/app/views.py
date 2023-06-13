from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app import lang, managedata, openai
# Create your views here.

def home(request):
    session = managedata.initialise("title")
    context = {
        "conversation_guid": session.guid
        }
    return render(request, "app/index.html", context)


@csrf_exempt
def prompt(request):
   
    user_message = request.POST.get('user_message', None)
    system_message = request.POST.get('system_message', None)
    title = request.POST.get('title', None)
    session_guid = request.POST.get('session_guid', None)
    print ("title received from api")
    print(title)
    
    print("session guid received at start of prompt view")
    print(session_guid)
    
    
   
    managedata.add_message(session, user_message, system_message, "user")
    
    
    """ lang_response = lang.query_chat(system_message, user_message, transcript)
    print("lang response")
    print(lang_response) """
    
    response_data = openai.chat4(system_message, user_message)
    print("openai response")
    print(response_data)
    
    response_content = {"content": response_data.content, "guid" : session_guid}
    return JsonResponse(response_content)