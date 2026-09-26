with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

mobile_farewell = """
@media (max-width: 768px) {
    .bright-light {
        width: 150px !important;
        height: 150px !important;
        left: -10px !important;
    }
    .main-fish {
        right: 180px !important;
        font-size: 4rem !important;
    }
    .fish-group {
        right: 20px !important;
        transform: scale(0.6) translateY(-50%) !important;
        transform-origin: center right;
    }
}
"""
css += mobile_farewell

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
