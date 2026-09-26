import re
with open('data.js', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("Makasih cong udah selalu ada buat gue. You are truly special!", "Thank you for coming into my life and being a part of it, Cong. 💛")

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(text)
