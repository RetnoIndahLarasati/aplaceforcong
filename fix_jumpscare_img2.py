import urllib.request
import base64
import re

url = "https://upload.wikimedia.org/wikipedia/commons/1/14/Anglerfish.jpg"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        img_data = response.read()

    b64 = base64.b64encode(img_data).decode('utf-8')
    data_uri = f"data:image/jpeg;base64,{b64}"

    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    html = re.sub(r'https://images.unsplash.com/photo-1560340798-93f5b084fb4d\?q=80&w=1000', data_uri, html)
    html = re.sub(r'\s*<a href="#gallery-section"', '\n          <a href="#map-section" class="nav-bubble">Treasure</a>\n          <a href="#gallery-section"', html)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Success")
except Exception as e:
    print("Error:", e)
