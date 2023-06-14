from GPT2Model.gpt2 import replyGPT2
from GPTNeo.gptneo import replyGPTNeo
from Bloom.bloom import replyBloom

import json as JSON
import random

f = r"Project\TextRefractoring\chatWhatsApp.json"

with open(f, "r", encoding="utf8") as f:
    chat = JSON.load(f)
    num = random.randint(0, len(chat) - 11)

    text = ""
    for i in range(10):
        text += list(chat[num+i].keys())[0] + ": " + chat[num+i][list(chat[num+i].keys())[0]].strip() + "\n"

    text += "Himir Desai: "

    print(replyBloom(text))