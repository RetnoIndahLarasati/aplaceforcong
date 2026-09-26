import re

with open('script.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "encodeURIComponent(" in line and "*Pesan Botol" in line:
        lines[i] = "                const waLink = `https://wa.me/${noWA}?text=${encodeURIComponent(\"🍾 *Pesan Botol dari Dasar Laut (Ocong)* 🍾\\n\\n\" + msg)}`;\n"
    # also remove any empty lines that were caused by the break
    if '" + msg)}`);' in line:
        lines[i] = ""

with open('script.js', 'w', encoding='utf-8') as f:
    f.writelines(lines)
