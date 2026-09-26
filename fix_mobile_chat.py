with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

mobile_chat = """
@media (max-width: 768px) {
    .floating-chat {
        width: 120px !important;
    }
}
"""
css += mobile_chat

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
