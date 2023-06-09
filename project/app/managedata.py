from app.models import Conversation, Messages

def initialise(title):
    
    
    newChat = Conversation.objects.create(
        title = title
    )
    
    print("new chat initialised")
    print (newChat)
    
    return newChat


def add_message(session, user_message, system_message, role):
   
    save_me = Messages.objects.create(
        conversation = session,
        prompt_value = user_message,
        system_value = system_message,
        role = role,
    )

    save_me.save()