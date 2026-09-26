import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

reply_section = """
        <!-- KIRIM BALIK PESAN -->
        <section id="reply-section" class="content-section" style="margin-top: 50px; text-align: center;">
            <h3 class="section-title">Kirim Balasan 🍾</h3>
            <p class="subtitle">Pesan balasan ini akan dimasukkan ke botol dan dihanyutkan kepadamu!</p>
            <div class="reply-container" style="position: relative; max-width: 600px; margin: 0 auto; padding: 20px;">
                <textarea id="reply-text" rows="5" placeholder="Tulis balasan rahasiamu untuk author di sini..." style="width: 100%; padding: 20px; border-radius: 15px; background: rgba(255,255,255,0.1); border: 2px solid rgba(255,255,255,0.3); color: white; font-family: 'Poppins', sans-serif; font-size: 1.1rem; backdrop-filter: blur(10px); resize: none; outline: none; box-sizing: border-box; transition: opacity 0.5s;"></textarea>
                <button id="send-reply-btn" class="action-btn" style="margin-top: 20px; font-size: 1.1rem; padding: 12px 30px; transition: opacity 0.5s;">Hanyutkan Botol 🌊</button>
                
                <div id="flying-bottle" style="position: absolute; top: 40%; left: 50%; transform: translate(-50%, -50%) scale(0.5); font-size: 5rem; opacity: 0; pointer-events: none; transition: all 2.5s cubic-bezier(0.25, 0.1, 0.25, 1); z-index: 10;">🍾</div>
            </div>
        </section>
"""

# Insert after message-section
html = re.sub(r'(<section id="message-section"[\s\S]*?</section>)', r'\1\n' + reply_section, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


with open('script.js', 'r', encoding='utf-8') as f:
    script = f.read()

reply_script = """
    // --- REPLY BOTTLE ---
    const sendReplyBtn = document.getElementById('send-reply-btn');
    const replyText = document.getElementById('reply-text');
    const flyingBottle = document.getElementById('flying-bottle');

    if (sendReplyBtn) {
        sendReplyBtn.addEventListener('click', () => {
            const msg = replyText.value.trim();
            if (!msg) {
                alert("Isi dulu pesannya yaa sebelum dihanyutkan!");
                return;
            }

            // Animate bottle (muncul)
            flyingBottle.style.opacity = '1';
            flyingBottle.style.transform = 'translate(-50%, -50%) scale(1)';
            
            // Sembunyikan textarea dan tombol pelan-pelan
            replyText.style.opacity = '0';
            sendReplyBtn.style.opacity = '0';
            
            // Animasi botol terbang menjauh
            setTimeout(() => {
                flyingBottle.style.transform = 'translate(100vw, -100vh) scale(0.2) rotate(70deg)';
                flyingBottle.style.opacity = '0';
            }, 1000);

            // Buka link WA / Email setelah animasi selesai
            setTimeout(() => {
                // --- UBAH NOMER WA DI BAWAH INI ---
                // Format: 628xxxxx (tanpa angka 0 di depan, tanpa tanda + atau spasi)
                const noWA = "6280000000000"; 
                
                const waLink = `https://wa.me/${noWA}?text=${encodeURIComponent("🍾 *Pesan Botol dari Dasar Laut (Ocong)* 🍾\\n\\n" + msg)}`;
                window.open(waLink, '_blank');
                
                // Reset UI kalau user balik ke web
                replyText.value = '';
                replyText.style.opacity = '1';
                sendReplyBtn.style.opacity = '1';
                flyingBottle.style.transition = 'none'; 
                flyingBottle.style.transform = 'translate(-50%, -50%) scale(0.5)';
                setTimeout(() => flyingBottle.style.transition = 'all 2.5s cubic-bezier(0.25, 0.1, 0.25, 1)', 50);
            }, 3500);
        });
    }
"""

# Insert before final surprise
script = re.sub(r'// --- FINAL SURPRISE ---', reply_script + '\n    // --- FINAL SURPRISE ---', script)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(script)
