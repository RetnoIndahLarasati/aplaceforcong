import re
with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

correct_script = """    // Mabar Photos
    const mabarContainer = document.getElementById('mabar-container');
    if (mabarContainer && oceanData.mabarPhotos) {
        oceanData.mabarPhotos.forEach((item) => {
            const card = document.createElement('div');
            card.className = 'mabar-card';
            card.innerHTML = `
                <img src="${item.image}" class="mabar-img" onerror="this.src='https://via.placeholder.com/400x300?text=Foto+Mabar'">
                <p class="mabar-caption">${item.caption}</p>
            `;
            mabarContainer.appendChild(card);
        });
    }

    // From To
    const ftContainer = document.getElementById('from-to-container');
    if (ftContainer && oceanData.fromTo) {
        ftContainer.innerHTML = `
            <div class="ft-card">
                <img src="${oceanData.fromTo.from.image}" class="ft-img" onerror="this.src='https://via.placeholder.com/300?text=Maba'">
                <p class="mabar-caption">${oceanData.fromTo.from.caption}</p>
            </div>
            <div class="ft-arrow">👉</div>
            <div class="ft-card">
                <img src="${oceanData.fromTo.to.image}" class="ft-img" onerror="this.src='https://via.placeholder.com/300?text=Dokter'">
                <p class="mabar-caption">${oceanData.fromTo.to.caption}</p>
            </div>
        `;
    }"""

# We need to replace the broken script which spans from // Mabar Photos to just before // Wishes
text = re.sub(r'// Mabar Photos[\s\S]*?// Wishes', correct_script + '\n\n    // Wishes', text)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(text)
