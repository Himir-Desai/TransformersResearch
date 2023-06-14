from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained('gpt2-medium')
model = GPT2LMHeadModel.from_pretrained('gpt2-medium')

def replyGPT2(text):
    encoded_input = tokenizer(text, return_tensors='pt', skip_special_tokens=True)
    maxl = len(encoded_input['input_ids'][0]) + 30
    output = model.generate(
        encoded_input['input_ids'],
        max_length=maxl,
        top_k=10, 
        top_p=0.10, 
        do_sample=True,
        )

    return tokenizer.decode(output[0])