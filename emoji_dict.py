emoji_dict = {
    "happy": "😃",
    "heart": "😍",
    "rotfl": "🤣",
    "smile": "😊",
    "crying": "😭",
    "kiss": "😘",
    "clap": "👏",
    "grin": "😁",
    "fire": "🔥",
    "broken": "💔",
    "think": "🤔",
    "excited": "🤩",
    "boring": "🙄",
    "winking": "😉",
    "ok": "👌",
    "hug": "🤗",
    "cool": "😎",
    "angry": "😠",
    "python": "🐍",
}

sentence = input("Please enter a sentence: ")
words = sentence.split()
for key, value in emoji_dict.items():
    for i, word in enumerate(words):
        if word == key:
            words[i] = emoji_dict[key]
           
result = " ".join(words)    
print(result)