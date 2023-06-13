import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")



def chat3turbo(user, system):    
    print("chat3turbo ran")
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": user},
        {"role": "system", "content": system}
    ]  
    )
    
    response = completion.choices[0].message
    return response

def chat4(user, system):
    print("chat4 ran")
    completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": user},
        {"role": "system", "content": system}
    ]
    )
    
    response = completion.choices[0].message
    return response