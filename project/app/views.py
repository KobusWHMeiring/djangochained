from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app import lang, managedata, openai
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
    #first word of the user's request.
    session_guid = request.POST.get('session_guid', None)
    
    #conversation object.  __str__ in this case wil be the title of the object
    session = Conversation.objects.get(guid = session_guid)
    managedata.add_message(session, user_message, system_message, "user")
    
    
    """ lang_response = lang.query_chat(system_message, user_message, transcript)
    print("lang response")
    print(lang_response) """
    
    response_data = openai.chat3turbo(system_message, user_message)
    managedata.add_message(session, response_data.content, "NA", "system")
    this_convo = Conversation.objects.get(guid = session.guid)
    convo_list = Messages.objects.filter(conversation = this_convo)
    
    
    for message in convo_list:
        print("message in convolist")
        print (message.prompt_value)
 
    print("openai response")
    print(response_data)
    
    response_content = {"content": response_data.content, "guid" : session_guid}
    return JsonResponse(response_content)