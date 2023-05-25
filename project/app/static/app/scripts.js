function handleSubmit(){
    value = document.getElementById("tool-selected").value
    console.log('value', value)
    if(value == "OCR" || value == "Dale-E" ){
        document.getElementById("modal-container").classList.remove("hidden")
        document.getElementById("main-options").classList.add("hidden")
    }
}


function acceptDisappointment(){
    document.getElementById("modal-container").classList.add("hidden")
    document.getElementById("main-options").classList.remove("hidden")
}