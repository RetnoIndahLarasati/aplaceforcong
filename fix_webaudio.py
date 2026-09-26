import re

with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove old audio globals
pattern_remove = r"const explosionSound = new Audio\('\./explosion\.mp3'\);\nconst popSound = new Audio\('\./pop\.mp3'\);\nconst fireworkSound = new Audio\('\./firework\.mp3'\);\n"
text = re.sub(pattern_remove, "", text)

# Add SoundFX
soundfx_code = """
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
const SoundFX = {
    pop: function() {
        if (audioCtx.state === 'suspended') audioCtx.resume();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.type = 'sine';
        osc.frequency.setValueAtTime(800, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(300, audioCtx.currentTime + 0.1);
        gain.gain.setValueAtTime(1, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.1);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.1);
    },
    explosion: function() {
        if (audioCtx.state === 'suspended') audioCtx.resume();
        const bufferSize = audioCtx.sampleRate * 1.5;
        const buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
            data[i] = Math.random() * 2 - 1;
        }
        const noise = audioCtx.createBufferSource();
        noise.buffer = buffer;
        const filter = audioCtx.createBiquadFilter();
        filter.type = 'lowpass';
        filter.frequency.value = 1000;
        const gain = audioCtx.createGain();
        noise.connect(filter);
        filter.connect(gain);
        gain.connect(audioCtx.destination);
        gain.gain.setValueAtTime(1, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 1.5);
        noise.start();
    },
    firework: function() {
        if (audioCtx.state === 'suspended') audioCtx.resume();
        const osc = audioCtx.createOscillator();
        const gain1 = audioCtx.createGain();
        osc.connect(gain1);
        gain1.connect(audioCtx.destination);
        osc.type = 'sine';
        osc.frequency.setValueAtTime(800, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(2000, audioCtx.currentTime + 1);
        gain1.gain.setValueAtTime(0.5, audioCtx.currentTime);
        gain1.gain.linearRampToValueAtTime(0, audioCtx.currentTime + 1);
        osc.start();
        osc.stop(audioCtx.currentTime + 1);
        setTimeout(() => this.explosion(), 1000);
    }
};
"""
text = soundfx_code + text

# Replace play calls
text = text.replace("explosionSound.currentTime = 0; explosionSound.play();", "SoundFX.explosion();")
text = text.replace("popSound.currentTime = 0; popSound.play();", "SoundFX.pop();")
text = text.replace("fireworkSound.currentTime = 0; fireworkSound.play();", "SoundFX.firework();")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(text)
