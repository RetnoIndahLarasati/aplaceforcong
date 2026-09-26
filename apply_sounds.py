import re

with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add sounds at the top
sounds = """
const explosionSound = new Audio('https://actions.google.com/sounds/v1/weapons/explosion_large.ogg');
const popSound = new Audio('https://actions.google.com/sounds/v1/foley/cork_pop.ogg');
const fireworkSound = new Audio('https://actions.google.com/sounds/v1/weapons/fireworks_with_whistle.ogg');
"""
text = text.replace("document.addEventListener('DOMContentLoaded', () => {", "document.addEventListener('DOMContentLoaded', () => {\n" + sounds)


# 2. Add explosion to bubble-secret
text = text.replace("if (this.id === 'bubble-secret') {\n\n                this.innerHTML", "if (this.id === 'bubble-secret') {\n                explosionSound.currentTime = 0; explosionSound.play();\n                this.innerHTML")


# 3. Add champagne pop to bottle
text = text.replace("bottle.addEventListener('click', () => {\n\n        openedMessage.classList.remove('hidden');\n\n    });", "bottle.addEventListener('click', () => {\n        popSound.currentTime = 0; popSound.play();\n        openedMessage.classList.remove('hidden');\n    });")


# 4. Add firework to setupFinalSurprise
text = text.replace("const triggerSurprise = () => {\n\n        finalChest.classList.add('hidden');", "const triggerSurprise = () => {\n        fireworkSound.currentTime = 0; fireworkSound.play();\n        finalChest.classList.add('hidden');")


# 5. Fix overlapping floating chats
old_chat_pos = """            const leftPos = 10 + (Math.random() * 60); 

            img.style.left = leftPos + "%";

            

            const delay = index * 0.8;"""
new_chat_pos = """            const spacing = 80 / Math.max(1, oceanData.chats.length - 1);
            const leftPos = 5 + (index * spacing); 
            img.style.left = leftPos + "%";
            
            // Stagger delay more and randomize vertical a bit with margin
            const delay = index * 1.5;"""
            
text = text.replace(old_chat_pos, new_chat_pos)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(text)
