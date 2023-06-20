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

    text = """
Ritvick Pandey: bro we cant take in everyone who is interested from the group, but i dont want to say anything eihter
Himir Desai: yeah thats why I am being silent
Ritvick Pandey: i think we should just take in the people who are interested and have the skills
"""
    text += "Himir Desai: "

    print(replyGPT2(text))