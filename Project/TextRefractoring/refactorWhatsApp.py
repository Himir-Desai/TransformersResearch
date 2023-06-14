import json as JSON

f = r"C:\Users\himir\TransformersResearch\Project\TextRefractoring\WhatsApp\_chat.txt"
chat = []

with open(f, "r", encoding="utf8") as f:
    for text in f:
        if '\u200e' not in text:
            P = text[text.find("]")+2:text.find(": ")]
            Message = text[text.find(": ")+2:]
            chat.append({P: Message})
        
f = r"C:\Users\himir\TransformersResearch\Project\TextRefractoring\chatWhatsApp.json"
with open(f, "w", encoding="utf8") as f:
    JSON.dump(chat, f, ensure_ascii=False, indent=4)
