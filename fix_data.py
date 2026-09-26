import re
with open('data.js', 'r', encoding='utf-8') as f:
    text = f.read()

new_memory = '''        {
            image: "https://images.unsplash.com/photo-1544644181-1484b3fdfc62?w=300&q=80",
            caption: "Tawa tak terlupakan",
            date: "Sometime"
        }'''

text = re.sub(r'(memories:\s*\[[\s\S]*?)(\s*\])', r'\1,\n' + new_memory + r'\2', text)

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(text)
