from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
model = AutoModelForMaskedLM.from_pretrained("bert-base-cased")

def replyBERT(text):
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