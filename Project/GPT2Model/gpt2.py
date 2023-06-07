from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
tokenizer = GPT2Tokenizer.from_pretrained('gpt2-large')
model = GPT2LMHeadModel.from_pretrained('gpt2-large')

def reply(text):
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model.generate(encoded_input['input_ids'], max_length=300)

    return tokenizer.decode(output[0])