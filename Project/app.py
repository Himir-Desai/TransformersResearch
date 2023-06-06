from GPT2Model.gpt2 import reply
import json as JSON

f = r"C:\Users\himir\TransformersResearch\Project\TextRefractoring\chatWhatsApp.json"

with open(f, "r", encoding="utf8") as f:
    chat = JSON.load(f)
    text = chat[2][list(chat[2].keys())[0]]
    print(reply(text))