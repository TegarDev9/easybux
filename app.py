import streamlit as st
import subprocess
import os
import requests
import time
import zipfile
import io

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
            # Mengunduh file zip ke dalam memori
            r = requests.get(repo_url, stream=True)
            r.raise_for_status() # Pastikan unduhan berhasil
            
            # Menggunakan zipfile untuk mengekstrak langsung dari memori
            with zipfile.ZipFile(io.BytesIO(r.content)) as z:
                z.extractall(".") # Ekstrak ke direktori saat ini
            
            # Ganti nama folder hasil ekstrak agar konsisten
            # Nama default dari GitHub adalah 'reponame-branchname'
            original_dir_name = "easybux-main" # Perhatikan, GitHub mengubah dari master ke main
            target_dir_name = "easybux-master" # Nama yang digunakan di sisa skrip
            
            # Hapus direktori target lama jika ada untuk menghindari error
            if os.path.exists(target_dir_name):
                 # Hapus direktori secara rekursif (jika diperlukan)
                import shutil
                shutil.rmtree(target_dir_name)

            # Ganti nama folder yang baru diekstrak
            if os.path.exists(original_dir_name):
                os.rename(original_dir_name, target_dir_name)

            st.success(f"Skrip berhasil diunduh dan diekstrak ke folder '{target_dir_name}'.")
            return True
        except zipfile.BadZipFile:
            st.error("Gagal mengekstrak file. File yang diunduh bukan file zip yang valid.")
            return False
        except requests.exceptions.RequestException as e:
            st.error(f"Gagal mengunduh repositori dari URL. Error: {e}")
            return False
        except Exception as e:
            st.error(f"Terjadi kesalahan saat memproses repo: {e}")
            return False

def main_app():
    """Fungsi untuk menampilkan antarmuka utama aplikasi setelah login berhasil."""
    st.title("🤖 EasyBux Bot Runner")
    st.caption("Menjalankan skrip 'bot.php' dari Inject-ID/easybux melalui antarmuka web.")
    
    st.sidebar.title("Navigasi")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    # --- UI Utama ---
    col1, col2 = st.columns([1, 2])

    with col1:
        st.header("⚙️ Pengaturan Bot")
        st.write("Isi konfigurasi berikut untuk menjalankan bot.")

        # Cek dan unduh direktori skrip
        script_dir = "easybux-master"
        if not os.path.exists(script_dir):
            st.warning("Direktori skrip 'easybux-master' tidak ditemukan.")
            if st.button("Unduh Skrip Sekarang"):
                if download_repo():
                    st.rerun()
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
                    
                    config_content = f'<?php\n$user_agent = "{user_agent}";\n$cookie = "{cookie}";\n?>'
                    try:
                        with open(os.path.join(script_dir, "config.php"), "w") as f:
                            f.write(config_content)
                        st.write("✅ File 'config.php' berhasil dibuat dengan kredensial Anda.")

                        process = subprocess.Popen(
                            ["php", "bot.php"],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True,
                            bufsize=1,
                            universal_newlines=True,
                            cwd=script_dir
                        )

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

                    except FileNotFoundError:
                        st.error("Perintah 'php' tidak ditemukan.")
                        st.warning(
                            "Pastikan 'php' terinstal. Jika menggunakan Streamlit Cloud, "
                            "tambahkan 'php' ke file 'packages.txt' Anda."
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
        3.  **Jalankan Bot**: Klik tombol "Jalankan Bot" dan pantau hasilnya di panel "Log Eksekusi".
        ---
        **Penting Mengenai Deteksi Bot:**
        * **Cookie adalah Kunci**: Cookie yang salah atau kedaluwarsa adalah penyebab kegagalan paling umum.
        * **Alamat IP**: Aplikasi ini berjalan di server Streamlit. Beberapa situs mungkin memblokir IP dari pusat data.
        * **Frekuensi Permintaan**: Penggunaan berlebihan dapat menyebabkan pemblokiran sementara oleh situs target.
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
