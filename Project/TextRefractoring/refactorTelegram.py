import json as JSON

f = r"C:\Users\himir\TransformersResearch\Project\TextRefractoring\Telegram\result.json"
chat = []

with open(f, "r", encoding="utf8") as f:
    data = JSON.load(f)
    for message in data["messages"]:
        if message["type"] == "message":
            chat.append({message["from"]: message["text"]})

f = r"C:\Users\himir\TransformersResearch\Project\TextRefractoring\chatTelegram.json"
with open(f, "w", encoding="utf8") as f:
    JSON.dump(chat, f, ensure_ascii=False, indent=4)