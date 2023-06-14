from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig



def flant5(prompt):
    
    prompt = prompt
    
    
    model_name = "google/flan-t5-base"
    #TODO explain wtf is going on here.
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    #use pytorch to get the tensors
    tokens = tokenizer(prompt, return_tensors="pt")
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    
    config = GenerationConfig(max_new_tokens=200)
    outputs = model.generate(**tokens, generation_config = config)
    #deocde the tokens that you get back from the model
    response = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    print("flan output!")
    print(response)
    return response
    
    #input_embeddings = model.get_input_embeddings()
    #token_ids = tokens['input_ids'][0]
     
    #our_embeddings = input_embeddings(token_ids)
    

