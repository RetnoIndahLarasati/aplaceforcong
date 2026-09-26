with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("window.addEventListener('load', () => {", "window.addEventListener('DOMContentLoaded', () => {")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(text)
