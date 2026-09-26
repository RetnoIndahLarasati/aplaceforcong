import re
with open('data.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the missing comma and chats: key
text = text.replace(']\n\n    // Chat Screenshots\n     [', '],\n\n    // Chat Screenshots\n    chats: [')

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(text)
