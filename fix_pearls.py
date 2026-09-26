import re

# 1. UPDATE INDEX.HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_reasons = '''        <section id="reasons-section" class="content-section">
            <h3 class="section-title">Mabar & Memories</h3>
            <p class="subtitle">Momen seru kita dan bukti perjalanan panjangmu!</p>
            
            <div class="mabar-container" id="mabar-container"></div>

            <h3 class="section-title" style="margin-top: 80px;">From This 👉 To This</h3>
            <div class="from-to-container" id="from-to-container"></div>
        </section>'''

html = re.sub(r'<section id="reasons-section"[\s\S]*?</section>', new_reasons, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. UPDATE STYLE.CSS
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = '''
/* ===== MABAR CARDS ===== */
.mabar-container {
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    justify-content: center;
    margin-top: 30px;
    width: 100%;
}
.mabar-card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 20px;
    width: 45%;
    min-width: 300px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    border: 1px solid rgba(255,255,255,0.2);
    display: flex;
    flex-direction: column;
    align-items: center;
    transition: transform 0.3s;
}
.mabar-card:hover {
    transform: translateY(-10px);
}
.mabar-img {
    width: 100%;
    height: 250px;
    object-fit: cover;
    border-radius: 15px;
    margin-bottom: 15px;
}
.mabar-caption {
    font-size: 1.1rem;
    line-height: 1.6;
    text-align: center;
    color: white;
}

/* ===== FROM THIS TO THIS ===== */
.from-to-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 40px;
    margin-top: 30px;
    flex-wrap: wrap;
}
.ft-card {
    background: rgba(2, 119, 189, 0.6);
    padding: 20px;
    border-radius: 20px;
    border: 2px dashed rgba(255,255,255,0.4);
    text-align: center;
    width: 300px;
}
.ft-img {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 10px;
    margin-bottom: 15px;
}
.ft-arrow {
    font-size: 4rem;
    color: white;
    text-shadow: 0 0 20px rgba(255,255,255,0.8);
    animation: bounceRight 2s infinite;
}
@keyframes bounceRight {
    0%, 100% { transform: translateX(0); }
    50% { transform: translateX(20px); }
}
@media (max-width: 768px) {
    .mabar-card { width: 100%; }
    .ft-arrow { transform: rotate(90deg); animation: bounceDown 2s infinite; }
    @keyframes bounceDown {
        0%, 100% { transform: translateY(0) rotate(90deg); }
        50% { transform: translateY(20px) rotate(90deg); }
    }
}
'''
css += new_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 3. UPDATE DATA.JS
with open('data.js', 'r', encoding='utf-8') as f:
    data = f.read()

new_data = '''    // Foto Mabar (Ganti Pearls of Truth)
    mabarPhotos: [
        {
            image: "./mabar1.jpeg",
            caption: "Caption panjang untuk foto mabar pertama. Tempat kamu tulis cerita seru pas mabar, ketawa-ketawa gajelas, atau drama saat main bareng yang gak terlupakan."
        },
        {
            image: "./mabar2.jpeg",
            caption: "Caption panjang untuk foto mabar kedua. Isi dengan keluh kesah atau kejadian epik yang terjadi pas kalian lagi push rank."
        },
        {
            image: "./mabar3.jpeg",
            caption: "Caption panjang untuk foto mabar ketiga. Mungkin foto karakter kalian di game atau momen ngakak lainnya."
        },
        {
            image: "./mabar4.jpeg",
            caption: "Caption panjang untuk foto mabar keempat. Kenangan berharga mabar sampai begadang."
        }
    ],

    // From This To This
    fromTo: {
        from: {
            image: "./maba.jpeg",
            caption: "Ocong jaman Maba (Masih polos dan plenger)"
        },
        to: {
            image: "./dokter.jpeg",
            caption: "Ocong jaman sekarang (Dokter Fisio yang keren abis!)"
        }
    },'''

# Replace reasons: array
data = re.sub(r'// Alasan kenapa dia spesial.*reasons: \[[^\]]*\],', new_data, data, flags=re.DOTALL)

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(data)

# 4. UPDATE SCRIPT.JS
with open('script.js', 'r', encoding='utf-8') as f:
    script = f.read()

new_script = '''    // Mabar Photos
    const mabarContainer = document.getElementById('mabar-container');
    if (mabarContainer && oceanData.mabarPhotos) {
        oceanData.mabarPhotos.forEach((item) => {
            const card = document.createElement('div');
            card.className = 'mabar-card';
            card.innerHTML = 
                <img src="" class="mabar-img" onerror="this.src='https://via.placeholder.com/400x300?text=Foto+Mabar'">
                <p class="mabar-caption"></p>
            ;
            mabarContainer.appendChild(card);
        });
    }

    // From To
    const ftContainer = document.getElementById('from-to-container');
    if (ftContainer && oceanData.fromTo) {
        ftContainer.innerHTML = 
            <div class="ft-card">
                <img src="" class="ft-img" onerror="this.src='https://via.placeholder.com/300?text=Maba'">
                <p class="mabar-caption"></p>
            </div>
            <div class="ft-arrow">👉</div>
            <div class="ft-card">
                <img src="" class="ft-img" onerror="this.src='https://via.placeholder.com/300?text=Dokter'">
                <p class="mabar-caption"></p>
            </div>
        ;
    }'''

# Replace reasons script logic
script = re.sub(r'// Reasons \(Clams\)[\s\S]*?// Wishes', new_script + '\\n\\n    // Wishes', script)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(script)

