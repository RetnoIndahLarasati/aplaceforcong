import re

with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the broken newlines in the string
bad_string_pattern = r'encodeURIComponent\("🍾 \*Pesan Botol dari Dasar Laut \(Ocong\)\* 🍾\n\n" \+ msg\)'
fixed_string = r'encodeURIComponent("🍾 *Pesan Botol dari Dasar Laut (Ocong)* 🍾\\n\\n" + msg)'
text = re.sub(bad_string_pattern, fixed_string, text)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(text)
