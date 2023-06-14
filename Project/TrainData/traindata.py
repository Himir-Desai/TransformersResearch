import json as JSON


f = r"Project\TextRefractoring\chatWhatsApp.json"

with open(f, "r", encoding="utf8") as f:
    chat = JSON.load(f)

    text = ""
    for i in range(len(chat)-1):
        text += list(chat[i].keys())[0] + ": " + chat[i][list(chat[i].keys())[0]].strip() + "\n"

with open(r"Project\TrainData\Data\chatWhatsApp.txt", "w", encoding="utf8") as f:
    f.write(text)   