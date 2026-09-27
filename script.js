
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


document.addEventListener('DOMContentLoaded', () => {



    // --- POPULATE DATA ---

    populateData();

    

    // --- HIDE LOADER ---

    setTimeout(() => {

        const loader = document.getElementById('loader');

        loader.style.opacity = '0';

        setTimeout(() => loader.style.display = 'none', 800);

    }, 1500);

    // --- BACKGROUND ANIMATIONS ---

    createOceanBackground();

    // --- DOM ELEMENTS ---

    const diveBtn = document.getElementById('dive-btn');

    const landing = document.getElementById('landing');

    const mainContent = document.getElementById('main-content');

    const navbar = document.getElementById('navbar');

    

    // --- AUDIO & PLAYLIST SETUP ---

    let audio = new Audio();

    let isPlaying = false;

    let currentSongIndex = 0;

    const playlist = oceanData.playlist || [];

    const musicPlayer = document.getElementById('music-player');

    const musicWidget = document.getElementById('music-widget');

    const closeMusicBtn = document.getElementById('close-music');

    

    // Widget elements

    const coverImg = document.getElementById('music-cover-img');

    const titleText = document.getElementById('music-title');

    const artistText = document.getElementById('music-artist');

    const btnPlayPause = document.getElementById('btn-play-pause');

    const btnPrev = document.getElementById('btn-prev');

    const btnNext = document.getElementById('btn-next');

    const progressBar = document.getElementById('progress-bar');

    const volumeBar = document.getElementById('volume-bar');

    const timeCurrent = document.getElementById('music-current');

    const timeDuration = document.getElementById('music-duration');

    function loadSong(index) {

        if (!playlist.length) return;

        const song = playlist[index];

        audio.src = song.file;

        titleText.textContent = song.title;

        artistText.textContent = song.artist;

        coverImg.src = song.cover;

    }

    if (playlist.length > 0) {

        loadSong(currentSongIndex);

    }

    // --- DIVE IN EVENT ---

    diveBtn.addEventListener("click", () => {

        const user = document.getElementById("login-username").value.trim();

        const pass = document.getElementById("login-password").value.trim();

        

        let isAdmin = false;

        if ((user === "Layla Widad Jamil" && pass === "29 Mei 2003") ||

            (user === "Retno Indah Larasati" && pass === "28 Juli 2006")) {

            isAdmin = true;

        }

        if (!isAdmin) {

            document.body.classList.add("guest-mode");

        }

        landing.classList.add("diving-out");

        

        setTimeout(() => {

            landing.style.display = "none";

            mainContent.classList.remove("hidden");

            navbar.classList.remove("hidden");

            document.getElementById("btn-play-game").classList.remove("hidden");
            const replyBtn = document.getElementById("btn-reply-msg"); if (replyBtn) replyBtn.classList.remove("hidden");

            window.scrollTo(0, 0);

            

            if (playlist.length > 0) {

                audio.play().then(() => {

                    isPlaying = true;

                    btnPlayPause.textContent = "⏸";

                    musicPlayer.classList.add("playing");

                }).catch(e => console.log("Audio autoplay prevented"));

            }

        }, 1000);

    });

    

    // --- MUSIC WIDGET CONTROLS ---

    // Open Widget

    musicPlayer.addEventListener("click", () => {

        musicWidget.classList.remove("hidden");

    });

    // Close Widget

    closeMusicBtn.addEventListener("click", () => {

        musicWidget.classList.add("hidden");

    });

    function togglePlay() {

        if (isPlaying) {

            audio.pause();
            btnPlayPause.textContent = "▶";

            musicPlayer.classList.remove("playing");

        } else {

            audio.play();

            btnPlayPause.textContent = "⏸";

            musicPlayer.classList.add("playing");

        }

        isPlaying = !isPlaying;

    }

    btnPlayPause.addEventListener("click", togglePlay);

    btnNext.addEventListener("click", () => {

        currentSongIndex = (currentSongIndex + 1) % playlist.length;

        loadSong(currentSongIndex);

        if (isPlaying) audio.play();

    });

    btnPrev.addEventListener("click", () => {

        currentSongIndex = (currentSongIndex - 1 + playlist.length) % playlist.length;

        loadSong(currentSongIndex);

        if (isPlaying) audio.play();

    });

    // Auto next on end

    audio.addEventListener("ended", () => {

        btnNext.click();

    });

    // Progress bar updates

    audio.addEventListener("timeupdate", () => {

        const current = audio.currentTime;

        const duration = audio.duration;

        if (duration) {

            progressBar.value = (current / duration) * 100;

            timeCurrent.textContent = formatTime(current);

            timeDuration.textContent = formatTime(duration);

        }

    });

    progressBar.addEventListener("input", (e) => {

        const seekTime = (e.target.value / 100) * audio.duration;

        audio.currentTime = seekTime;

    });

    // Volume control

    volumeBar.addEventListener("input", (e) => {

        audio.volume = e.target.value;

    });

    function formatTime(seconds) {

        if (isNaN(seconds)) return "0:00";

        const m = Math.floor(seconds / 60);

        const s = Math.floor(seconds % 60);

        return `${m}:${s < 10 ? "0" : ""}${s}`;

    }

    // --- INTERACTIVE ELEMENTS ---

    setupInteractiveElements();

    // --- BOTTLE MESSAGE ---

    const bottle = document.getElementById('message-bottle');

    const openedMessage = document.getElementById('opened-message');

    const closeBtn = document.getElementById('close-message');

    bottle.addEventListener('click', () => {
        SoundFX.pop();
        openedMessage.classList.remove('hidden');
    });

    closeBtn.addEventListener('click', () => {

        openedMessage.classList.add('hidden');

    });

    // --- LIGHTBOX ---

    setupLightbox();

    
    
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
    const jumpscareOverlay = document.getElementById('jumpscare-overlay');
    let jumpscareTriggered = false;

    if (subSlider && treasureReveal) {
        subSlider.addEventListener('input', (e) => {
            const val = parseInt(e.target.value);
            
            
            if (val < 35 || val > 75) {
                jumpscareTriggered = false; // Reset!
            }

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
                const noWA = "6287781849128"; 
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
// --- FINAL SURPRISE ---

    setupFinalSurprise();

    // --- CLICK BUBBLES EFFECT ---

    document.addEventListener('click', (e) => {

        // Create 3-5 bubbles

        const count = Math.floor(Math.random() * 3) + 3;

        for (let i = 0; i < count; i++) {

            const bubble = document.createElement('div');

            bubble.className = 'click-bubble';

            

            // Randomize slight offset from cursor

            const offsetX = (Math.random() - 0.5) * 30;

            const offsetY = (Math.random() - 0.5) * 30;

            

            bubble.style.left = (e.clientX + offsetX) + 'px';

            bubble.style.top = (e.clientY + offsetY) + 'px';

            

            // Random size

            const size = Math.random() * 15 + 5;

            bubble.style.width = size + 'px';

            bubble.style.height = size + 'px';

            

            document.body.appendChild(bubble);

            

            // Remove after animation completes (1s)

            setTimeout(() => {

                bubble.remove();

            }, 1000);

        }

    });

    // --- FAREWELL SCENE ---

    const btnStartFarewell = document.getElementById("btn-start-farewell");

    const btnReplayFarewell = document.getElementById("btn-replay-farewell");

    const brightLight = document.getElementById("bright-light");

    const mainFish = document.getElementById("main-fish");

    

    let bubbleInterval;

    function playFarewell() {

        btnStartFarewell.classList.add("hidden");

        btnReplayFarewell.classList.add("hidden");

        

        // Nyalakan cahaya terang

        brightLight.classList.add("active");

        

        // Setelah 1.5 detik saling menatap, ikan utama berbalik dan berenang pergi

        setTimeout(() => {

            mainFish.classList.add("leaving");

            // Ikan berenang ke arah kiri (cahaya)

            mainFish.style.right = "110%";

            mainFish.style.opacity = "0"; 

            

            // Efek gelembung ngikutin ikan saat berenang

            bubbleInterval = setInterval(() => {

                makeBubbles(mainFish);

            }, 500); // Tiap setengah detik keluar gelembung

            

            // Setelah 8 detik, animasi berenang selesai

            setTimeout(() => {

                clearInterval(bubbleInterval);

                btnReplayFarewell.classList.remove("hidden");

            }, 8000);

            

        }, 1500);

    }

    

    function resetFarewell() {

        brightLight.classList.remove("active");

        mainFish.classList.remove("leaving");

        mainFish.style.right = "250px";

        mainFish.style.opacity = "1";

        btnReplayFarewell.classList.add("hidden");

        btnStartFarewell.classList.remove("hidden");

    }

    btnStartFarewell.addEventListener("click", playFarewell);

    btnReplayFarewell.addEventListener("click", resetFarewell);

    // --- CHAT NET SURPRISE ---

    const netTrigger = document.getElementById("net-trigger");

    const floatingChatsContainer = document.getElementById("floating-chats-container");

    const trappedFish = document.querySelector(".trapped-fish");

    const netIcon = document.querySelector(".net-icon");

    let netBroken = false;

    netTrigger.addEventListener("click", () => {

        if(netBroken) return;

        netBroken = true;

        

        // Break net & free fish

        netIcon.style.opacity = "0";

        netIcon.style.transition = "opacity 1s";

        

        trappedFish.style.animation = "swim-across 5s forwards";

        

        // Spawn chats

        if(oceanData.chats) {

            oceanData.chats.forEach((chatUrl, index) => {

                const img = document.createElement("img");

                img.src = chatUrl;

                img.className = "floating-chat";

                

                // Spaced evenly across the screen to prevent overlap
                const spacing = 80 / Math.max(1, oceanData.chats.length - 1);
                const leftPos = 5 + (index * spacing); 
                img.style.left = leftPos + "%";
                
                // Stagger delay more so they go up one by one
                const delay = index * 1.5;

                img.style.animationDelay = delay + "s";

                

                // Randomize float speed

                const duration = 12 + (Math.random() * 8); // 12s to 20s

                img.style.animationDuration = duration + "s";

                

                // Add lightbox click event

                img.addEventListener("click", () => {

                    const lightbox = document.getElementById("lightbox");

                    const lbImg = document.getElementById("lightbox-img");

                    lbImg.src = chatUrl;

                    document.getElementById("lightbox-caption").textContent = "Memori Chat";

                    lightbox.classList.remove("hidden");

                });

                

                floatingChatsContainer.appendChild(img);

                

                // Start animation

                setTimeout(() => {

                    img.classList.add("released");

                }, 10);

            });

        }

    });

    // --- SCROLL SPY FOR NAVBAR ---

    const sections = document.querySelectorAll('.content-section');

    const navLinks = document.querySelectorAll('.nav-bubble');

    const observer = new IntersectionObserver((entries) => {

        entries.forEach(entry => {

            if (entry.isIntersecting) {

                // Hapus class active dari semua menu

                navLinks.forEach(link => link.classList.remove('active'));

                

                // Tambahkan class active ke menu yang sesuai dengan section yang sedang terlihat

                const activeId = entry.target.id;

                const activeLink = document.querySelector(`.nav-bubble[href="#${activeId}"]`);

                if (activeLink) {

                    activeLink.classList.add('active');

                }

            }

        });

    }, { threshold: 0.3 }); // Memicu ketika 30% section terlihat

    sections.forEach(sec => observer.observe(sec));

});

// FUNCTIONS

function populateData() {

    // Name

    const nameSpans = document.querySelectorAll('.personal-name');

    nameSpans.forEach(span => span.textContent = oceanData.name);

    // Greeting

    const greetingText = document.getElementById('greeting-text');

    const surpriseGreeting = document.getElementById('surprise-greeting-text');

    if (greetingText) greetingText.textContent = oceanData.greeting || "Happy Birthday";

    if (surpriseGreeting) surpriseGreeting.textContent = oceanData.greeting || "Happy Birthday";

    // Personal Message

    const msgText = document.getElementById('personal-message-text');

    msgText.textContent = oceanData.birthdayMessage;

    // Memories (Fishes carrying photos)

    const memoriesContainer = document.getElementById('memories-container');

    const carrierEmojis = ['🐡', '🐠', '🐟', '🦈', '🦀', '🦑'];

    

    oceanData.memories.forEach((mem) => {

        const carrier = document.createElement('div');

        carrier.className = 'fish-carrier';

        

        // Random direction (50% chance to go right-to-left)

        const isReverse = Math.random() > 0.5;

        if (isReverse) {

            carrier.classList.add('flip-direction');

        }

        

        // Random emoji

        const emoji = carrierEmojis[Math.floor(Math.random() * carrierEmojis.length)];

        

        // Random vertical position (5% to 30% supaya bener-bener aman dari bawah)

        const top = Math.random() * 25 + 5;

        carrier.style.top = `${top}%`;

        

        // Random speed (15s to 35s to cross screen)

        const duration = Math.random() * 20 + 15; 

        

        // Random delay (dibuat negatif semua supaya tidak ada yang diam nunggu giliran jalan)

        const delay = -(Math.random() * 40); 

        

        carrier.style.animationDuration = `${duration}s`;

        carrier.style.animationDelay = `${delay}s`;

        

        // Slight random rotation for the polaroid frame

        const rot = Math.random() * 14 - 7; 

        

        carrier.innerHTML = `

            <div class="carrier-icon">${emoji}</div>

            <div class="polaroid" style="transform: rotate(${rot}deg)">

                <img src="${mem.image}" alt="Memory" class="polaroid-img" onerror="this.src='https://via.placeholder.com/300?text=Photo'">

                <div class="polaroid-caption">${mem.caption}</div>

                <div class="polaroid-date">${mem.date}</div>

            </div>

        `;

        memoriesContainer.appendChild(carrier);

        

        carrier.addEventListener("click", () => {

            const isPaused = carrier.style.animationPlayState === "paused";

            carrier.style.animationPlayState = isPaused ? "running" : "paused";

        });

    });

            // Mabar Photos
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

    // Wishes (Jellyfish)

    const jellyContainer = document.getElementById('jellyfish-container');

    if(oceanData.wishes) {

        oceanData.wishes.forEach((wish) => {

            const jelly = document.createElement('div');

            jelly.className = 'jellyfish';

            jelly.innerHTML = `

                <span class="jelly-icon">🪼</span>

                <div class="jelly-msg">${wish}</div>

            `;

            // random animation delay so they don't float synchronously

            jelly.style.animationDelay = `${Math.random() * 2}s`;

            

            jelly.addEventListener('click', function() {

                this.classList.toggle('clicked');

                if(this.classList.contains('clicked')) {

                    setTimeout(() => this.classList.remove('clicked'), 4000);

                }

            });

            jellyContainer.appendChild(jelly);

        });

    }

    // Gallery

    const galleryContainer = document.getElementById('gallery-container');

    galleryContainer.innerHTML = '';

    oceanData.gallery.forEach((pic) => {

        const item = document.createElement('div');

        item.className = 'gallery-item';

        item.innerHTML = `

            <img src="${pic.image}" alt="Gallery image" onerror="this.src='https://via.placeholder.com/300?text=Photo'" data-caption="${pic.caption}">

        `;

        galleryContainer.appendChild(item);

    });

}

function createOceanBackground() {

    const bgContainer = document.getElementById('ocean-background');

    const emojis = ['🐡', '🐠', '🐟', '🐙', '🦀', '🦑'];

    

    for (let i = 0; i < 20; i++) createBubble(bgContainer);

    for (let i = 0; i < 6; i++) createFish(bgContainer, emojis);

}

function createBubble(container) {

    const bubble = document.createElement('div');

    bubble.className = 'bg-bubble';

    

    const size = Math.random() * 15 + 5;

    const left = Math.random() * 100;

    const duration = Math.random() * 10 + 5; 

    const delay = Math.random() * 10;

    

    bubble.style.width = `${size}px`;

    bubble.style.height = `${size}px`;

    bubble.style.left = `${left}%`;

    bubble.style.animationDuration = `${duration}s`;

    bubble.style.animationDelay = `${delay}s`;

    

    container.appendChild(bubble);

}

function createFish(container, emojis) {

    const fish = document.createElement('div');

    fish.className = 'bg-fish';

    

    const isRightToLeft = Math.random() > 0.5;

    if (isRightToLeft) {

        fish.classList.add('flip-x');

        fish.style.animationDirection = 'reverse';

    }

    

    const emoji = emojis[Math.floor(Math.random() * emojis.length)];

    fish.textContent = emoji;

    

    const top = Math.random() * 80 + 10; 

    const duration = Math.random() * 20 + 15; 

    const delay = Math.random() * 5;

    const size = Math.random() * 1.5 + 1; 

    

    fish.style.top = `${top}%`;

    fish.style.fontSize = `${size}rem`;

    fish.style.animationDuration = `${duration}s`;

    fish.style.animationDelay = `${delay}s`;

    

    container.appendChild(fish);

}

function setupInteractiveElements() {

    const interactives = document.querySelectorAll('.interactive-element');

    interactives.forEach(el => {

        el.addEventListener('click', function() {

            this.style.transform = 'scale(0.9)';

            setTimeout(() => this.style.transform = '', 150);

            const popup = this.querySelector('.popup-msg');

            if (popup) {

                popup.classList.toggle('hidden');

                setTimeout(() => popup.classList.add('hidden'), 3000);

            }

            

            if (this.id === 'bubble-secret') {
                SoundFX.explosion();
                this.innerHTML = '💥';

                setTimeout(() => {

                    this.innerHTML = '<span class="icon">🫧</span>';

                }, 1000);

            }

        });

    });

}

function setupLightbox() {

    const lightbox = document.getElementById('lightbox');

    const lbImg = document.getElementById('lightbox-img');

    const lbCaption = document.getElementById('lightbox-caption');

    const lbClose = document.getElementById('lightbox-close');

    

    document.getElementById('gallery-container').addEventListener('click', (e) => {

        if (e.target.tagName === 'IMG') {

            lbImg.src = e.target.src;

            lbCaption.textContent = e.target.getAttribute('data-caption') || '';

            lightbox.classList.remove('hidden');

        }

    });

    const closeLightbox = () => lightbox.classList.add('hidden');

    lbClose.addEventListener('click', closeLightbox);

    lightbox.addEventListener('click', (e) => {

        if (e.target === lightbox) closeLightbox();

    });

}

function setupFinalSurprise() {

    const finalChest = document.getElementById('final-chest');

    const surpriseContent = document.getElementById('surprise-content');

    const replayBtn = document.getElementById('replay-btn');

    const triggerSurprise = () => {
        SoundFX.firework();
        finalChest.classList.add('hidden');

        surpriseContent.classList.remove('hidden');

        

        const duration = 3 * 1000;

        const animationEnd = Date.now() + duration;

        const defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 0 };

        function randomInRange(min, max) {

            return Math.random() * (max - min) + min;

        }

        const interval = setInterval(function() {

            const timeLeft = animationEnd - Date.now();

            if (timeLeft <= 0) return clearInterval(interval);

            const particleCount = 50 * (timeLeft / duration);

            confetti(Object.assign({}, defaults, { 

                particleCount,

                origin: { x: randomInRange(0.1, 0.9), y: Math.random() - 0.2 },

                colors: ['#89E4E4', '#FFB347', '#ffffff', '#1AB5D8']

            }));

        }, 250);

    };

    finalChest.addEventListener('click', triggerSurprise);

    replayBtn.addEventListener('click', () => {

        surpriseContent.classList.add('hidden');

        finalChest.classList.remove('hidden');

    });

   function makeBubbles(fish) {

    for (let i = 0; i < 6; i++) {

        const bubble = document.createElement("span");

        bubble.classList.add("click-bubble");

        bubble.style.left = "50%";

        bubble.style.top = "30%";

        bubble.style.setProperty(

            "--bubble-x",

            `${(Math.random() - 0.5) * 70}px`

        );

        bubble.style.animationDelay = `${i * 0.1}s`;

        fish.appendChild(bubble);

        setTimeout(() => {

            bubble.remove();

        }, 2000);

        document.querySelectorAll(".fish").forEach(fish => {

    fish.addEventListener("click", () => {

        makeBubbles(fish);

    });

});

    }

   }

}

