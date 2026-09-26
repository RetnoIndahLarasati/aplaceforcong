import re

with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix overlapping chats
pattern = r'const leftPos = 10 \+ \(Math\.random\(\) \* 60\);\s*img\.style\.left = leftPos \+ "%";\s*const delay = index \* 0\.8;'
replacement = """const spacing = 80 / Math.max(1, oceanData.chats.length - 1);
            const leftPos = 5 + (index * spacing); 
            img.style.left = leftPos + "%";
            const delay = index * 1.5;"""
text = re.sub(pattern, replacement, text)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(text)
