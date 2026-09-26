import re
with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find("const waLink = `https://wa.me/${noWA}?text=${encodeURIComponent(\"🍾 *Pesan Botol dari Dasar Laut (Ocong)* 🍾")
if start_idx != -1:
    end_idx = text.find(";\n", start_idx) + 1
    new_text = text[:start_idx] + "const waLink = `https://wa.me/${noWA}?text=${encodeURIComponent(\"🍾 *Pesan Botol dari Dasar Laut (Ocong)* 🍾\\\\n\\\\n\" + msg)}`;" + text[end_idx:]
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(new_text)
