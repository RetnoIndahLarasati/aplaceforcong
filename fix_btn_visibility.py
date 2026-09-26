import re
with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Make sure btn-reply-msg is shown on login
text = text.replace('document.getElementById("btn-play-game").classList.remove("hidden");', 'document.getElementById("btn-play-game").classList.remove("hidden");\n            const replyBtn = document.getElementById("btn-reply-msg"); if (replyBtn) replyBtn.classList.remove("hidden");')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(text)
