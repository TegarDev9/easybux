import streamlit as st
import subprocess
import os
import requests
import time
import zipfile
import io
import shutil

# --- Konfigurasi Aplikasi ---
st.set_page_config(page_title="EasyBux Bot Runner", layout="wide", initial_sidebar_state="collapsed")

# --- Fungsi dan Logika Aplikasi ---

def check_credentials(username, password):
    """Fungsi sederhana untuk memeriksa kredensial login."""
    # Ganti username dan password ini sesuai keinginan Anda
    return username == "Tegarkaruniailham" and password == "Tegarilham4444"

def download_repo():
    """Mengunduh dan mengekstrak repositori menggunakan pustaka Python."""
    repo_url = "https://github.com/Inject-ID/easybux/archive/refs/heads/main.zip"
    with st.spinner("Mengunduh skrip dari GitHub... Ini mungkin perlu waktu sejenak."):
        try:
            r = requests.get(repo_url, stream=True)
            r.raise_for_status()
            
            with zipfile.ZipFile(io.BytesIO(r.content)) as z:
                z.extractall(".")
            
            original_dir_name = "easybux-main"
            target_dir_name = "easybux-master"
            
            if os.path.exists(target_dir_name):
                shutil.rmtree(target_dir_name)

            if os.path.exists(original_dir_name):
                os.rename(original_dir_name, target_dir_name)

            st.success(f"Skrip berhasil diunduh dan diekstrak ke folder '{target_dir_name}'.")
            return True
        except Exception as e:
            st.error(f"Terjadi kesalahan saat memproses repo: {e}")
            return False

def setup_dummy_xdg_open():
    """Membuat file xdg-open palsu untuk mencegah error di lingkungan server."""
    xdg_open_path = os.path.join(os.getcwd(), "xdg-open")
    if not os.path.exists(xdg_open_path):
        with open(xdg_open_path, "w") as f:
            f.write("#!/bin/sh\n")
            f.write("echo 'Mencegat panggilan xdg-open: '$@\n")
            f.write("exit 0\n")
        # Membuat file dapat dieksekusi
        os.chmod(xdg_open_path, 0o755)

def main_app():
    """Fungsi untuk menampilkan antarmuka utama aplikasi setelah login berhasil."""
    st.title("🤖 EasyBux Bot Runner")
    st.caption("Menjalankan skrip 'bot.php' dari Inject-ID/easybux melalui antarmuka web.")
    
    st.sidebar.title("Navigasi")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    # Panggil fungsi untuk membuat xdg-open palsu
    setup_dummy_xdg_open()

    # --- UI Utama ---
    col1, col2 = st.columns([1, 2])

    with col1:
        st.header("⚙️ Pengaturan Bot")
        st.write("Isi konfigurasi berikut untuk menjalankan bot.")

        script_dir = "easybux-master"
        if not os.path.exists(script_dir):
            st.warning("Direktori skrip 'easybux-master' tidak ditemukan.")
            if st.button("Unduh Skrip Sekarang"):
                if download_repo():
                    st.rerun()
        else:
            st.success("Direktori skrip 'easybux-master' sudah siap.")

        # Opsi menu yang akan dikirim ke skrip bot.php
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
            
            st.subheader("2. Pilih Tugas Bot")
            pilihan_tugas = st.radio(
                "Pilih tugas yang ingin dijalankan:",
                options=list(bot_options.keys()),
                help="Opsi ini akan dikirim sebagai input ke skrip PHP."
            )
            
            submit_button = st.form_submit_button(label="🚀 Jalankan Bot")

        if submit_button:
            if not cookie:
                st.warning("Harap masukkan cookie Anda.")
            elif not os.path.exists(os.path.join(script_dir, 'bot.php')):
                st.error("File 'bot.php' tidak ditemukan. Coba unduh ulang skrip.")
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

                        # Menyiapkan environment khusus untuk subprocess
                        my_env = os.environ.copy()
                        # Menambahkan direktori saat ini ke PATH agar xdg-open palsu ditemukan
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
                            env=my_env  # Menggunakan environment yang telah dimodifikasi
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
                        if stderr_output:
                            st.error("Pesan Error dari Skrip:")
                            st.code(stderr_output, language="bash")

                    except Exception as e:
                        st.error(f"Terjadi kesalahan yang tidak terduga: {e}")

    with col2:
        st.header("💡 Cara Penggunaan & Tips")
        st.markdown("""
        1.  **Unduh Skrip**: Jika diminta, klik tombol "Unduh Skrip Sekarang".
        2.  **Isi Formulir**: Masukkan `User Agent` dan `Cookie` Anda, lalu pilih tugas bot.
        3.  **Jalankan Bot**: Klik tombol "Jalankan Bot" dan pantau hasilnya di panel "Log Eksekusi".
        ---
        **PENTING: Menyesuaikan Nomor Pilihan**
        * Skrip ini mengasumsikan bahwa 'Auto Claim' adalah **opsi nomor 3** di menu `bot.php`.
        * Jika di skrip aslinya nomornya berbeda (misalnya nomor 2 atau 4), Anda perlu **mengubahnya di kode Python** pada bagian `bot_options`.
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
