from app.models import Conversation, Messages

def initialise(title):
    
    
    newChat = Conversation.objects.create(
        title = title
    )
    
    
    
    return newChat


def add_message(session,system_message, user_message, role):
    save_me = Messages.objects.create(
        conversation = session,
        prompt_value = user_message,
        system_value = system_message,
        role = role,
    )
    
    save_me.save()