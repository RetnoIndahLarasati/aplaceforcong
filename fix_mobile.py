import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

mobile_fixes = """
@media (max-width: 768px) {
    /* Pindah navbar ke bawah biar ga tabrakan sama tombol Play & Balas */
    #navbar {
        top: auto !important;
        bottom: 20px;
        flex-wrap: wrap;
    }
    
    /* Geser music player ke atas dikit */
    #music-player {
        bottom: 90px !important;
    }

    /* Sesuaikan ukuran tombol kiri atas */
    .play-btn {
        top: 15px !important;
        left: 15px !important;
        font-size: 0.8rem !important;
        padding: 6px 12px !important;
    }
    .reply-btn {
        top: 15px !important;
        left: 105px !important;
        font-size: 0.8rem !important;
        padding: 6px 12px !important;
    }
}
"""

css += mobile_fixes

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
