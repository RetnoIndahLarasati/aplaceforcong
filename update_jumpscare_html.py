import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change treasure reveal text
old_reveal = r"""<div id="treasure-reveal".*?>[\s\S]*?</div>"""
new_reveal = """<div id="treasure-reveal" style="opacity: 0; transform: translateY(20px); transition: all 1s; margin-top: 30px;">
                    <h2 style="color: gold; font-family: 'Fredoka', sans-serif; font-size: 2.5rem; letter-spacing: 2px;">GUE BENCI BGT SAMA LU <3</h2>
                </div>"""
html = re.sub(r'<div id="treasure-reveal"[\s\S]*?</p>\s*</div>', new_reveal, html)

# Add jumpscare overlay before </body>
jumpscare_html = """
    <!-- JUMPSCARE OVERLAY -->
    <div id="jumpscare-overlay" class="hidden" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: black; z-index: 9999; display: flex; justify-content: center; align-items: center;">
        <img src="https://images.unsplash.com/photo-1560340798-93f5b084fb4d?q=80&w=1000" style="width: 100vw; height: 100vh; object-fit: cover; filter: contrast(150%) sepia(100%) hue-rotate(300deg);">
    </div>
"""

html = html.replace("</body>", jumpscare_html + "\n</body>")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
