import re
with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'// Randomize horizontal position around the net \(10% to 70%\)[\s\S]*?const leftPos = 10 \+ \(Math\.random\(\) \* 60\);\s*img\.style\.left = leftPos \+ "%";[\s\S]*?// Stagger the animation[\s\S]*?const delay = index \* 0\.8;'

replacement = """// Spaced evenly across the screen to prevent overlap
                const spacing = 80 / Math.max(1, oceanData.chats.length - 1);
                const leftPos = 5 + (index * spacing); 
                img.style.left = leftPos + "%";
                
                // Stagger delay more so they go up one by one
                const delay = index * 1.5;"""

text = re.sub(pattern, replacement, text)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(text)
