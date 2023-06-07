from GPT2Model.gpt2 import reply
import json as JSON
import random

f = r"C:\Users\himir\TransformersResearch\Project\TextRefractoring\chatTelegram.json"

with open(f, "r", encoding="utf8") as f:
    chat = JSON.load(f)
    num = random.randint(0, len(chat) - 6)
    text = list(chat[num+1].keys())[0] + ": " + chat[num+1][list(chat[num+1].keys())[0]].strip() + "\n"
    text += list(chat[num+2].keys())[0] + ": " + chat[num+2][list(chat[num+2].keys())[0]].strip() + "\n"
    text += list(chat[num+3].keys())[0] + ": " + chat[num+3][list(chat[num+3].keys())[0]].strip() + "\n"
    text += list(chat[num+4].keys())[0] + ": " + chat[num+4][list(chat[num+4].keys())[0]].strip() + "\n"
    text += list(chat[num+5].keys())[0] + ": " + chat[num+5][list(chat[num+5].keys())[0]].strip() + "\n"

    text += "Himir: "

    print(reply(text))