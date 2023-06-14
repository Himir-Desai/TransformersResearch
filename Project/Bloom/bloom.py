from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("bigscience/bloom-560m")
model = AutoModelForCausalLM.from_pretrained("bigscience/bloom-560m")

def replyBloom(text):
    encoded_input = tokenizer(text, return_tensors='pt')
    maxl = len(encoded_input['input_ids'][0]) + 30
    output = model.generate(
        encoded_input['input_ids'],
        max_length=maxl,
        top_k=10, 
        top_p=0.10, 
        do_sample=True,
        )

    return tokenizer.decode(output[0])