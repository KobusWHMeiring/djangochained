import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")



def chat3turbo(user, system, transcript):
    transcript = transcript
    if transcript:   
        print("trnscript!")
        print(transcript)
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": user},
        {"role": "system", "content": system}
    ]
    
    )
    
    response = completion.choices[0].message
    print(response)
    return response

def chat4(user, system):
    
    """ if transcript:   
        print("trnscript!")
        print(transcript) """
    
    completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": user},
        {"role": "system", "content": system}
    ]
    
    )
    
    response = completion.choices[0].message
    print(response)
    return response