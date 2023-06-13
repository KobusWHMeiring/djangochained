function initialiseConvo(){
    addEventListener("DOMContentLoaded", (event) => {
        let hello = "world"
    });
}


function sendMessage(){
    let systemMessage = document.getElementById("system-prompt").value
    let userMessage = document.getElementById("user-prompt").value
    
    document.getElementById("user-prompt").value = ""
    console.log('systemMessage', systemMessage)
    console.log('userMessage', userMessage)
    prompt = {"system": systemMessage, "user": userMessage}
    document.getElementById("send-button").innerHTML = "Sent!"
    let title = "Niksnie"
    convoobject = document.getElementById("conversation").innerHTML
    
    console.log('convoobject', convoobject)

    if (convoobject == ""){
        console.log('convoobject to check if title needs to be created', convoobject)
        var words = userMessage.split(" "); // Split the string by spaces
        var firstWord = words[0];
        title = firstWord
    }
    showUserMessage(userMessage, systemMessage)
    

    let config = {
        type: "POST",
        url: '/prompt/',
        data: {
            'user_message': userMessage,
            'system_message': systemMessage, 
            'title': title,
        
        },
        dataType: 'json',
        success: function(response){
            console.log("successs")
            console.log(response)
            showMessage(response.content)
            console.log('response.guid', response.guid)
            story = story + response.content
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

    newMessage.innerHTML = message
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