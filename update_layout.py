import re

# ==========================================
# 1. MODIFY HTML
# ==========================================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Floating Reply Button right after Play It button
btn_reply = '<button id="btn-reply-msg" class="reply-btn hidden">Balas 💌</button>'
html = re.sub(r'(<button id="btn-play-game"[^>]*>.*?</button>)', r'\1\n    ' + btn_reply, html)

# Replace the #reply-section in the flow with #map-section
map_section = """
        <!-- PETA HARTA KARUN INTERAKTIF -->
        <section id="map-section" class="content-section" style="margin-top: 50px; text-align: center;">
            <h3 class="section-title">Treasure Map 🗺️</h3>
            <p class="subtitle">Geser kapal selam ke tanda ❌ untuk membuka harta karun!</p>
            <div class="map-container" style="position: relative; max-width: 600px; margin: 30px auto; padding: 40px 20px; background: rgba(2, 119, 189, 0.4); border: 2px dashed rgba(255,255,255,0.5); border-radius: 20px;">
                <input type="range" id="submarine-slider" min="0" max="100" value="0" style="width: 80%; margin-bottom: 20px; cursor: pointer;">
                <div style="display: flex; justify-content: space-between; width: 80%; margin: 0 auto; font-size: 1.5rem;">
                    <span>🌊</span>
                    <span>❌</span>
                </div>
                
                <div id="treasure-reveal" style="opacity: 0; transform: translateY(20px); transition: all 1s; margin-top: 30px;">
                    <h2 style="color: gold; font-family: 'Fredoka', sans-serif;">🎉 Selamat Ocong! 🎉</h2>
                    <p style="color: white; font-size: 1.1rem; line-height: 1.6;">Semua pencapaianmu sampai titik ini adalah harta karun yang paling berharga. Keep sailing! 🌊</p>
                </div>
            </div>
        </section>
"""

# Find and extract the inner content of reply-section to put into an overlay
reply_overlay = """
    <!-- REPLY OVERLAY MODAL -->
    <div id="reply-overlay" class="hidden" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0,0,0,0.8); z-index: 2000; display: flex; flex-direction: column; justify-content: center; align-items: center;">
        <button id="close-reply-modal" style="position: absolute; top: 20px; right: 20px; font-size: 2rem; background: none; border: none; color: white; cursor: pointer;">❌</button>
        <h3 class="section-title" style="margin-bottom: 10px;">Kirim Balasan 🍾</h3>
        <p class="subtitle" style="margin-bottom: 30px;">Pesan ini akan dihanyutkan langsung ke WhatsApp author!</p>
        <div style="position: relative; width: 90%; max-width: 500px; padding: 20px; background: rgba(2,119,189,0.5); border: 2px solid rgba(255,255,255,0.3); border-radius: 15px; backdrop-filter: blur(10px); text-align: center;">
            <textarea id="reply-text" rows="5" placeholder="Tulis pesan rahasiamu di sini..." style="width: 100%; padding: 15px; border-radius: 10px; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.5); color: white; font-family: 'Poppins', sans-serif; font-size: 1.1rem; resize: none; outline: none; box-sizing: border-box; transition: opacity 0.5s;"></textarea>
            <button id="send-reply-btn" class="action-btn" style="margin-top: 20px; font-size: 1.1rem; padding: 12px 30px; transition: opacity 0.5s;">Hanyutkan Botol 🌊</button>
            
            <div id="flying-bottle" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%) scale(0.5); font-size: 5rem; opacity: 0; pointer-events: none; transition: all 2.5s cubic-bezier(0.25, 0.1, 0.25, 1); z-index: 10;">🍾</div>
        </div>
    </div>
"""

# Replace reply-section with map-section in the flow
html = re.sub(r'<!-- KIRIM BALIK PESAN -->[\s\S]*?</section>', map_section, html)

# Add reply overlay right before </body>
html = html.replace('</body>', reply_overlay + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# ==========================================
# 2. MODIFY CSS
# ==========================================
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

btn_css = """
/* ===== REPLY BUTTON ===== */
.reply-btn {
    position: fixed;
    top: 20px;
    right: 20px;
    background: rgba(255, 152, 0, 0.8);
    color: white;
    border: 2px solid white;
    padding: 10px 20px;
    border-radius: 20px;
    font-weight: bold;
    font-family: "Poppins", sans-serif;
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    transition: all 0.3s ease;
    z-index: 1001;
    cursor: pointer;
}
.reply-btn:hover {
    background: white;
    color: #ff9800;
    transform: scale(1.1);
}

/* ===== SLIDER ===== */
#submarine-slider {
    -webkit-appearance: none;
    height: 10px;
    background: rgba(255,255,255,0.2);
    border-radius: 5px;
    outline: none;
}
#submarine-slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 40px;
    height: 40px;
    background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><text y="50" font-size="50">🛥️</text></svg>') no-repeat center center;
    background-size: contain;
    cursor: pointer;
    transform: translateY(-10px);
}
"""

css += btn_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)


# ==========================================
# 3. MODIFY SCRIPT
# ==========================================
with open('script.js', 'r', encoding='utf-8') as f:
    script = f.read()

# Make the play and reply buttons visible when logged in
script = script.replace("document.getElementById('btn-play-game').classList.remove('hidden');", "document.getElementById('btn-play-game').classList.remove('hidden');\n                const replyBtn = document.getElementById('btn-reply-msg'); if (replyBtn) replyBtn.classList.remove('hidden');")

# Fix the modal open/close logic and add map logic
modal_logic = """
    // --- REPLY MODAL LOGIC ---
    const btnReplyMsg = document.getElementById('btn-reply-msg');
    const replyOverlay = document.getElementById('reply-overlay');
    const closeReplyModal = document.getElementById('close-reply-modal');
    
    if (btnReplyMsg && replyOverlay) {
        btnReplyMsg.addEventListener('click', () => {
            replyOverlay.classList.remove('hidden');
        });
        closeReplyModal.addEventListener('click', () => {
            replyOverlay.classList.add('hidden');
        });
    }

    // --- TREASURE MAP LOGIC ---
    const subSlider = document.getElementById('submarine-slider');
    const treasureReveal = document.getElementById('treasure-reveal');
    if (subSlider && treasureReveal) {
        subSlider.addEventListener('input', (e) => {
            if (e.target.value > 90) {
                treasureReveal.style.opacity = '1';
                treasureReveal.style.transform = 'translateY(0)';
                SoundFX.pop(); // Mainin suara pop pas kebuka
            } else {
                treasureReveal.style.opacity = '0';
                treasureReveal.style.transform = 'translateY(20px)';
            }
        });
    }
"""

# Replace the existing REPLY BOTTLE logic
pattern_reply_bottle = r'// --- REPLY BOTTLE ---[\s\S]*?(?=// --- FINAL SURPRISE ---)'
new_reply_bottle = modal_logic + """
    // --- REPLY BOTTLE SEND LOGIC ---
    const sendReplyBtn = document.getElementById('send-reply-btn');
    const replyText = document.getElementById('reply-text');
    const flyingBottle = document.getElementById('flying-bottle');

    if (sendReplyBtn && replyText && flyingBottle) {
        sendReplyBtn.addEventListener('click', () => {
            const msg = replyText.value.trim();
            if (!msg) {
                alert("Isi dulu pesannya yaa sebelum dihanyutkan!");
                return;
            }

            flyingBottle.style.opacity = '1';
            flyingBottle.style.transform = 'translate(-50%, -50%) scale(1)';
            replyText.style.opacity = '0';
            sendReplyBtn.style.opacity = '0';
            
            setTimeout(() => {
                flyingBottle.style.transform = 'translate(100vw, -100vh) scale(0.2) rotate(70deg)';
                flyingBottle.style.opacity = '0';
                SoundFX.explosion(); // Suara meluncur
            }, 1000);

            setTimeout(() => {
                // --- UBAH NOMER WA DI BAWAH INI ---
                const noWA = "6280000000000"; 
                const waLink = `https://wa.me/${noWA}?text=${encodeURIComponent("🍾 *Pesan Botol dari Dasar Laut (Ocong)* 🍾\\n\\n" + msg)}`;
                window.open(waLink, '_blank');
                
                // Reset UI & Close Modal
                replyText.value = '';
                replyText.style.opacity = '1';
                sendReplyBtn.style.opacity = '1';
                flyingBottle.style.transition = 'none'; 
                flyingBottle.style.transform = 'translate(-50%, -50%) scale(0.5)';
                replyOverlay.classList.add('hidden');
                setTimeout(() => flyingBottle.style.transition = 'all 2.5s cubic-bezier(0.25, 0.1, 0.25, 1)', 50);
            }, 3500);
        });
    }
"""

script = re.sub(pattern_reply_bottle, new_reply_bottle, script)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(script)

