import re

# 1. Update data.js
with open('data.js', 'r', encoding='utf-8') as f:
    data = f.read()

new_msg = r"""birthdayMessage: `Cong, selamat buat sumpah profesi lo yaaa! Asal looooo tau gue sebangga itu kayak SEBANGGA ITU paham gaks? Sayang aja kabar semembanggakan ini ga lu kabari ke gue langsung hiks </3 Walaupun lu merasa moment itu buat lu biasa aja tetep kabarin gue yaa, Cong. Lu hari pertama kerja aja ngabarin dengan segala struggle lo itu, kenapa yang ini ngga?! Gue kan udah pernah bilang sama lu, kabar sekecil apapun dari lu update ke gue juga (kalo bisa) coba aja lu ngasih tau ke gue lebih awal, gue pengen banget hadir di situuuu tauk :(\n\nStruggle lu buat sampe jadi lu yang sekarang gue tau ga gampang, banyak pilihan, banyak masalahnya, tapi syukurnya semua bisa lu handle dengan baik, i knowww, i trust u since day 1. Ihk agak alay tapi gue suka tiba-tiba terharu ya kenal lu dari SMA terus ke Maba Plenger, terus sekarang tiba-tiba udah Sumpah Profesi dan gue dari Bokem SMP, Anomali UTBK, sampe sekarang jadi Tiang PLN, udah grow bareng-bareng, SEBARENG ITUH.\n\nDan sekarang, lo udah sampai di titik yang dulu mungkin cuma jadi salah satu hal yang harus lo lewatin. Hari ini, lo bukan cuma selesai dari satu proses, tapi juga udah mulai satu perjalanan baru sebagai seorang profesional (ancis). Sumpah yang lo ucapin hari ini gue harap bukan cuma sekedar seremoni atau formalitas, tapi jadi sesuatu yang bakal lo inget setiap kali nanti ketemu hari-hari yang susah dalam perjalanan profesi lo.\n\nOlah semua mulai dari ilmu, perjuangan, dan semua hal yang udah lo lewatin sampai di titik ini buat jadi bekal buat lo ke depannya. Semoga lo selalu jadi orang yang tetap punya hati di tengah kesibukan, tetap inget alasan kenapa lo mulai di awal, dan yang ga kalah penting, bangga sama diri lo sendiri meskipun nanti jalannya nggak selalu gampang.\n\nSo, congrats ya Conggg. You really made it. Gue bangga banget bisa ngeliat salah satu fase hidup lo sampai sejauh ini, dan semoga gue masih dikasih umur dan kesemparan untuk terus denger cerita-cerita lo di fase-fase berikutnya. Dari struggle, cerita anomali lo itu, sampe ke TMI yang menurut lo mungkin nggak penting penting bgt ntuh, kabarin gue terus yaaa. Karena buat gue, cerita dari lo nggak pernah sekecil itu!\n\nLu udah membuktikan skill lu saat gue konsul sih cong, padahal gue bukan konsultasi yang gimana gimana bgt tapi lu sampe nanyain dan sampe ngechat (bahkan nyari) klinik yang bagus, and i'm so grateful and feels so amazing punya temen yang perhatian kayak lu. Makasih seribu makasih ya, Cong. Gue kayaknya bakal terus update per-syraf kejepitan ini sama lu deh wkwwkwk sampe sembuh sampe ada perubahan.\n\nKedepannya lu sakses selalu ya, apapun yang lu laluin, apapun yang lu rasain, berbagi ke orang-orang ya cong. Jangan semua muanya di keep sendiri, jangan sombonggg lu kuat dan segala macem, cuma lu sendiri yang tau keadaan dan kapasitas lu sendiri, okeh?\n\nOmongan gue selanjutnya mungkin bakal klasik dan basi banget buat diucapin. Tapi beneran deh, lu tuh udah gue anggep kayak kakak sendiri, yang beneran kakak. Walaupun baru ketemu 2 kali dan cuma ngehabisin waktu di RL total sekitar 5-6 hari tapi semua waktu yang dihabisin sama lu bener-bener meaningful banget buat gue.\n\nCong, gue selalu seneng dan bahagia bgt bisa ngehabisin waktu sama lu. Pas lagi bikin ini gue tiba-tiba kepikiran tau what if entah di another life gitu atau another universe kita bakal ketemu ga yaah? TAPI GAMAU AHK, maunya ketemuan lagii sama lu walaupun cara kenalannya agak mustahil (kita aja sebenernya mustahil juga awalnya) dan agak aneh gapapa, hope we always find our way back to each other, and get to know each other again.\n\nMakasih cong udah selalu ada buat gue. You are truly special!`"""

data = re.sub(r'birthdayMessage: `.*?`', new_msg, data, flags=re.DOTALL)

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(data)

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the navbar order
old_nav = """        <a href="#message-section" class="nav-bubble">Message</a>
        <a href="#chat-section" class="nav-bubble">Chats</a>
          <a href="#map-section" class="nav-bubble">Treasure</a>"""
new_nav = """        <a href="#message-section" class="nav-bubble">Message</a>
        <a href="#map-section" class="nav-bubble">Treasure</a>
        <a href="#chat-section" class="nav-bubble">Chats</a>"""

html = html.replace(old_nav, new_nav)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
