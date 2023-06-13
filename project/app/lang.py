from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage
)
import requests

chat = ChatOpenAI()
llm = OpenAI(model_name = "text-davinci-003", temperature=0.8)


def query_chat(system, user, transcript):
    
    transcript = transcript
    user_prompt = user
    system_prompt = system
    
    if transcript: 
        user_prompt = "You have been having the following conversation: " + transcript + "the user has now asked the following: " + user_prompt
        print("transcript happened, new user prompt: ")
        print(user_prompt)
    
   
    
    prompt = user_prompt.replace("<TRANSCRIPT>", user)
   
   
   
   
   
   
   
    print("system prompt just before langchain prints")
    print(system_prompt)
    messages = [
    SystemMessage(content=system_prompt),
    HumanMessage(content=prompt)
        ]
    
    response = chat(messages)
    print("lang function success")
    """ send_whatsapp(response) """
    return response



def send_whatsapp(message):
    

    

    response = requests.post(url, headers=headers, json=data)
    print(response.text)


def edit_mode(system, user):
    
    
    messages = [
    SystemMessage(content=system),
    HumanMessage(content=user)
        ]
    
    response = chat(messages)
    print("lang function success")
    return response
