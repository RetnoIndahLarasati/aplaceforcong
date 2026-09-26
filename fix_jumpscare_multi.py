import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Unsplash with local foto6
html = re.sub(r'https://images.unsplash.com/photo-1560340798-93f5b084fb4d\?q=80&w=1000', './foto6.jpeg', html)

# Add nav if not added yet
if "Treasure</a>" not in html:
    html = re.sub(r'\s*<a href="#gallery-section"', '\n          <a href="#map-section" class="nav-bubble">Treasure</a>\n          <a href="#gallery-section"', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Make it trigger multiple times
multi_trigger = """
            if (val < 35 || val > 75) {
                jumpscareTriggered = false; // Reset!
            }

            // JUMPSCARE AT 50%
"""
text = text.replace("// JUMPSCARE AT 50%", multi_trigger)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(text)
