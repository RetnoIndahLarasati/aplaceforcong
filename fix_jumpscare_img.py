import urllib.request
import base64

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Anglerfish.jpg/800px-Anglerfish.jpg"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    img_data = response.read()

b64 = base64.b64encode(img_data).decode('utf-8')
data_uri = f"data:image/jpeg;base64,{b64}"

import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the unsplash image with the base64 anglerfish
html = re.sub(r'https://images.unsplash.com/photo-1560340798-93f5b084fb4d\?q=80&w=1000', data_uri, html)

# Add Treasure to nav
nav_link = '          <a href="#map-section" class="nav-bubble">Treasure</a>\n          <a href="#gallery-section"'
html = re.sub(r'\s*<a href="#gallery-section"', '\n' + nav_link, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
