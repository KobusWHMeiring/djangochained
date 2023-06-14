from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app import lang, managedata, openai, managemodels
from app.models import Conversation, Messages
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
    model = request.POST.get('model', None)
    #first word of the user's request.
    session_guid = request.POST.get('session_guid', None)
    
    #conversation object.  __str__ in this case wil be the title of the object
    session = Conversation.objects.get(guid = session_guid)
    this_convo = Conversation.objects.get(guid = session.guid)
    transcript = Messages.transcript(this_convo)
    managedata.add_message(session, user_message, system_message, "user")
    
    response_data = managemodels.sendModel(user_message, system_message, transcript, model)
    print("response data in views")
    print(response_data)
    
    if model == "google_flan":
        managedata.add_message(session, response_data, "NA", "system")
        response_content = {"content": response_data, "guid" : session_guid}
        
    else: 
        managedata.add_message(session, response_data.content, "NA", "system")
        response_content = {"content": response_data.content, "guid" : session_guid}
   
    
   
    return JsonResponse(response_content)