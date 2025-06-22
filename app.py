import streamlit as st
import subprocess
import os
import requests
import time

# --- Konfigurasi Aplikasi ---
st.set_page_config(page_title="EasyBux Bot Runner", layout="wide", initial_sidebar_state="collapsed")

# --- Fungsi dan Logika Aplikasi ---

def check_credentials(username, password):
    """Fungsi sederhana untuk memeriksa kredensial login."""
    # Ganti username dan password ini sesuai keinginan Anda
    return username == "Tegarkaruniailham" and password == "Tegarilham4444"

def download_repo():
    """Mengunduh dan mengekstrak repositori skrip dari GitHub."""
    repo_url = "https://github.com/Inject-ID/easybux/archive/refs/heads/main.zip"
    with st.spinner("Mengunduh skrip dari GitHub... Ini mungkin perlu waktu sejenak."):
        try:
            # Mengunduh file zip
            r = requests.get(repo_url, stream=True)
            r.raise_for_status()
            with open("easybux.zip", "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # Mengekstrak file zip
            # Perintah '-o' akan menimpa file tanpa bertanya
            subprocess.run(["unzip", "-o", "easybux.zip"], check=True, capture_output=True)
            
            # Menghapus file zip setelah diekstrak
            os.remove("easybux.zip")
            st.success("Skrip berhasil diunduh dan diekstrak ke folder 'easybux-master'.")
            return True
        except subprocess.CalledProcessError as e:
            st.error(f"Gagal mengekstrak file. Pastikan 'unzip' terinstal. Error: {e.stderr.decode()}")
            return False
        except Exception as e:
            st.error(f"Gagal mengunduh repositori: {e}")
            return False

def main_app():
    """Fungsi untuk menampilkan antarmuka utama aplikasi setelah login berhasil."""
    st.title("🤖 EasyBux Bot Runner")
    st.caption("Menjalankan skrip 'bot.php' dari Inject-ID/easybux melalui antarmuka web.")
    
    # Tombol Logout
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    # --- UI Utama ---
    col1, col2 = st.columns([1, 2])

    with col1:
        st.header("⚙️ Pengaturan Bot")
        st.write("Skrip ini memerlukan beberapa input dari Anda untuk berjalan dengan benar.")

        # Cek dan unduh direktori skrip
        script_dir = "easybux-master"
        if not os.path.exists(script_dir):
            st.warning("Direktori skrip 'easybux-master' tidak ditemukan.")
            if st.button("Unduh Skrip Sekarang"):
                if download_repo():
                    st.rerun() # Muat ulang halaman untuk memperbarui status
        else:
            st.success("Direktori skrip 'easybux-master' sudah siap.")

        # Formulir Konfigurasi
        with st.form("bot_config_form"):
            user_agent = st.text_input(
                "User Agent", 
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                help="Gunakan User Agent dari browser yang Anda gunakan untuk login."
            )
            cookie = st.text_area("Cookie", help="Masukkan cookie dari sesi login Anda di situs EasyBux.")
            
            submit_button = st.form_submit_button(label="🚀 Jalankan Bot")

        if submit_button:
            if not cookie:
                st.warning("Harap masukkan cookie Anda.")
            elif not os.path.exists(os.path.join(script_dir, 'bot.php')):
                st.error("File 'bot.php' tidak ditemukan. Coba unduh ulang skrip.")
            else:
                with col2:
                    st.header("📝 Log Eksekusi")
                    st.info("Mempersiapkan dan menjalankan skrip 'bot.php'...")
                    
                    # Membuat file config.php yang diperlukan oleh bot.php
                    config_content = f'<?php\n$user_agent = "{user_agent}";\n$cookie = "{cookie}";\n?>'
                    try:
                        with open(os.path.join(script_dir, "config.php"), "w") as f:
                            f.write(config_content)
                        st.write("✅ File 'config.php' berhasil dibuat dengan kredensial Anda.")

                        # Menjalankan skrip PHP menggunakan subprocess
                        process = subprocess.Popen(
                            ["php", os.path.join(script_dir, "bot.php")],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True,
                            bufsize=1,
                            universal_newlines=True,
                            cwd=script_dir # Menjalankan perintah dari dalam direktori skrip
                        )

                        # Menampilkan output secara real-time
                        output_placeholder = st.empty()
                        log_output = ""
                        for line in iter(process.stdout.readline, ''):
                            log_output += line
                            output_placeholder.code(log_output, language="bash")
                        
                        process.stdout.close()
                        return_code = process.wait()
                        
                        st.success("Eksekusi skrip selesai.")

                        # Menampilkan error jika ada
                        stderr_output = process.stderr.read()
                        if stderr_output:
                            st.error("Pesan Error dari Skrip:")
                            st.code(stderr_output, language="bash")

                    except FileNotFoundError:
                        st.error("Perintah 'php' tidak ditemukan.")
                        st.warning(
                            "Pastikan PHP terinstal di lingkungan. Jika menggunakan Streamlit Cloud, "
                            "tambahkan 'php' dan 'unzip' ke file 'packages.txt' Anda."
                        )
                    except Exception as e:
                        st.error(f"Terjadi kesalahan yang tidak terduga: {e}")

    with col2:
        st.header("💡 Cara Penggunaan & Tips")
        st.markdown("""
        1.  **Unduh Skrip**: Jika diminta, klik tombol "Unduh Skrip Sekarang".
        2.  **Isi Formulir**:
            * **User Agent**: Sebaiknya gunakan User Agent dari browser yang sama saat Anda mengambil cookie.
            * **Cookie**: Ini adalah bagian terpenting. Dapatkan dari *Developer Tools* (F12) di browser Anda setelah login ke EasyBux.
        3.  **Jalankan Bot**: Klik tombol "Jalankan Bot" dan pantau hasilnya di panel "Log Eksekusi" di sebelah kanan.

        ---
        **Penting Mengenai Deteksi Bot:**
        * **Cookie adalah Kunci**: Cookie yang salah atau kedaluwarsa adalah penyebab kegagalan paling umum.
        * **Alamat IP**: Aplikasi ini berjalan di server Streamlit. Beberapa situs mungkin memblokir IP dari pusat data.
        * **Frekuensi Permintaan**: Skrip ini mungkin membuat permintaan dengan cepat. Penggunaan berlebihan dapat menyebabkan pemblokiran sementara.
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
                st.success("Login berhasil!")
                time.sleep(1) # Jeda sejenak agar pesan terlihat
                st.rerun()
            else:
                st.error("Username atau password salah.")

