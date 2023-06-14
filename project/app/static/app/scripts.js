function initialiseConvo(){
    addEventListener("DOMContentLoaded", (event) => {
        let hello = "world"
    });
}


function sendMessage(){
    let systemMessage = document.getElementById("system-prompt").value
    let userMessage = document.getElementById("user-prompt").value
    let models = document.getElementById("models").value
    
    document.getElementById("user-prompt").value = ""
    prompt = {"system": systemMessage, "user": userMessage}

    document.getElementById("send-button").innerHTML = "Sent!"
    let title = "Niksnie"
    convoobject = document.getElementById("conversation").innerHTML
    
    
    

    showUserMessage(userMessage, systemMessage)
    

    let config = {
        type: "POST",
        url: '/prompt/',
        data: {
            'user_message': userMessage,
            'system_message': systemMessage, 
            'session_guid': conversationGuid,
            'model': models,
        },
        dataType: 'json',
        success: function(response){
            console.log("successs")
            console.log(response)
            showMessage(response.content)
            console.log('response.guid', response.guid)
            document.getElementById("send-button").innerHTML = "Send"
           /*  createNewChat() */

        }
    }

    $.ajax(config);

  
}

function showMessage(message){
    newMessage = document.createElement('div')
    newMessage.innerHTML = message

    document.getElementById("conversation").appendChild(newMessage)
}

function showUserMessage(message, system){
    newMessage = document.createElement('div')
    newMessage.classList.add("user-message")
    newMessage.innerHTML = "User Message: "+ message
    newSysMessage = document.createElement('div')
    system = "System Prompt: " + system
    newSysMessage.innerHTML = system
    document.getElementById("conversation").appendChild(newSysMessage)
    document.getElementById("conversation").appendChild(newMessage)
}

/* function createNewChat(){
    newElement = document.createElement('div')
    newElement.classList.add('prompt-container')

    document.getElementById("content-container").appendChild(newElement)
} */

function handleKeyDown(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
}