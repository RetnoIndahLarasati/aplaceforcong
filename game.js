document.addEventListener('DOMContentLoaded', () => {
    const btnPlayGame = document.getElementById('btn-play-game');
    const overlay = document.getElementById('game-overlay');
    const btnClose = document.getElementById('btn-close-game');
    const player = document.getElementById('player-salmon');
    const gameArea = document.getElementById('game-area');
    const winScreen = document.getElementById('game-win');
    const btnRestart = document.getElementById('btn-restart-game');
    
    let isPlaying = false;
    let playerX = 50;
    let playerY = window.innerHeight / 2;
    let bears = [];
    let animationFrame;
    
    if(!btnPlayGame) return;

    btnPlayGame.addEventListener('click', startGame);
    btnClose.addEventListener('click', stopGame);
    btnRestart.addEventListener('click', resetGame);
    
    function startGame() {
        overlay.classList.remove('hidden');
        resetGame();
    }
    
    function stopGame() {
        overlay.classList.add('hidden');
        isPlaying = false;
        cancelAnimationFrame(animationFrame);
    }
    
    function resetGame() {
        isPlaying = true;
        playerX = 50;
        player.style.left = playerX + 'px';
        winScreen.classList.add('hidden');
        
        // Clear bears
        bears.forEach(b => b.element.remove());
        bears = [];
        
        // Create new bears
        const cols = window.innerWidth > 800 ? 7 : 4;
        const spacing = window.innerWidth / (cols + 1);
        for(let i=1; i<=cols; i++) {
            createBear(spacing * i);
        }
        
        gameLoop();
    }
    
    function createBear(x) {
        const el = document.createElement('div');
        el.className = 'enemy-bear';
        el.textContent = '🐻';
        el.style.left = x + 'px';
        gameArea.appendChild(el);
        
        bears.push({
            element: el,
            x: x,
            y: Math.random() * window.innerHeight,
            speed: (Math.random() * 5 + 3) * (Math.random() > 0.5 ? 1 : -1)
        });
    }
    
    gameArea.addEventListener('mousemove', (e) => {
        if(!isPlaying) return;
        playerY = e.clientY;
        player.style.top = playerY + 'px';
    });

    // For mobile touch
    gameArea.addEventListener('touchmove', (e) => {
        if(!isPlaying) return;
        playerY = e.touches[0].clientY;
        player.style.top = playerY + 'px';
    }, {passive: true});
    
    gameArea.addEventListener('click', () => {
        if(!isPlaying) return;
        playerX += window.innerWidth > 600 ? 60 : 40; // Swim forward!
        player.style.left = playerX + 'px';
    });
    
    function gameLoop() {
        if(!isPlaying) return;
        
        // Move bears
        bears.forEach(bear => {
            bear.y += bear.speed;
            if(bear.y < 0 || bear.y > window.innerHeight) {
                bear.speed *= -1; // Bounce
            }
            bear.element.style.top = bear.y + 'px';
            
            // Check collision
            const pRect = player.getBoundingClientRect();
            const bRect = bear.element.getBoundingClientRect();
            
            // Hitbox shrink for fairness
            if (pRect.left + 15 < bRect.right - 15 &&
                pRect.right - 15 > bRect.left + 15 &&
                pRect.top + 15 < bRect.bottom - 15 &&
                pRect.bottom - 15 > bRect.top + 15) {
                // Dead
                playerX = 50;
                player.style.left = playerX + 'px';
            }
        });
        
        // Check win
        if(playerX > window.innerWidth - 80) {
            isPlaying = false;
            winScreen.classList.remove('hidden');
        } else {
            animationFrame = requestAnimationFrame(gameLoop);
        }
    }
});
