import re

with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

scream_code = """
    scream: function() {
        if (audioCtx.state === 'suspended') audioCtx.resume();
        const osc = audioCtx.createOscillator();
        const osc2 = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sawtooth';
        osc2.type = 'square';
        osc.frequency.setValueAtTime(200, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(3000, audioCtx.currentTime + 0.1);
        osc2.frequency.setValueAtTime(300, audioCtx.currentTime);
        osc2.frequency.exponentialRampToValueAtTime(4000, audioCtx.currentTime + 0.1);
        osc.connect(gain);
        osc2.connect(gain);
        gain.connect(audioCtx.destination);
        gain.gain.setValueAtTime(3, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 1.5);
        osc.start();
        osc2.start();
        osc.stop(audioCtx.currentTime + 1.5);
        osc2.stop(audioCtx.currentTime + 1.5);
    },
    explosion: function() {
"""

text = text.replace("    explosion: function() {", scream_code)

map_logic = """
    // --- TREASURE MAP LOGIC ---
    const subSlider = document.getElementById('submarine-slider');
    const treasureReveal = document.getElementById('treasure-reveal');
    const jumpscareOverlay = document.getElementById('jumpscare-overlay');
    let jumpscareTriggered = false;

    if (subSlider && treasureReveal) {
        subSlider.addEventListener('input', (e) => {
            const val = parseInt(e.target.value);
            
            // JUMPSCARE AT 50%
            if (val > 45 && val < 60 && !jumpscareTriggered) {
                jumpscareTriggered = true;
                if (jumpscareOverlay) jumpscareOverlay.classList.remove('hidden');
                SoundFX.scream();
                setTimeout(() => {
                    if (jumpscareOverlay) jumpscareOverlay.classList.add('hidden');
                }, 1000);
            }

            if (val > 90) {
                treasureReveal.style.opacity = '1';
                treasureReveal.style.transform = 'translateY(0)';
            } else {
                treasureReveal.style.opacity = '0';
                treasureReveal.style.transform = 'translateY(20px)';
            }
        });
    }
"""

text = re.sub(r'// --- TREASURE MAP LOGIC ---[\s\S]*?// --- REPLY BOTTLE SEND LOGIC ---', map_logic + '\n    // --- REPLY BOTTLE SEND LOGIC ---', text)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(text)
