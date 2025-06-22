import streamlit as st
import subprocess
import os
import requests
import time

# --- Konfigurasi dan Tampilan Aplikasi ---
st.set_page_config(page_title="EasyBux Bot Runner", layout="wide")

st.title("🤖 EasyBux Bot Runner")
st.caption("Menjalankan skrip 'bot.php' dari Inject-ID/easybux melalui antarmuka web.")

# --- Fungsi untuk mengunduh repositori ---
def download_repo():
    repo_url = "https://github.com/Inject-ID/easybux/archive/refs/heads/master.zip"
    with st.spinner("Mengunduh skrip dari GitHub..."):
        try:
            r = requests.get(repo_url, stream=True)
            r.raise_for_status()
            with open("easybux.zip", "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # Ekstrak file zip
            subprocess.run(["unzip", "-o", "easybux.zip"], check=True)
            
            # Hapus file zip setelah diekstrak
            os.remove("easybux.zip")
            st.success("Skrip berhasil diunduh dan diekstrak ke folder 'easybux-master'.")
            return True
        except Exception as e:
            st.error(f"Gagal mengunduh repositori: {e}")
            return False

# --- UI Utama ---
# Kolom untuk tata letak yang lebih baik
col1, col2 = st.columns([1, 2])

with col1:
    st.header("⚙️ Pengaturan")
    st.write("Skrip ini memerlukan beberapa input dari Anda untuk berjalan dengan benar.")

    # Cek apakah direktori skrip sudah ada
    script_dir = "easybux-master"
    if not os.path.exists(script_dir):
        st.warning("Direktori skrip 'easybux-master' tidak ditemukan.")
        if st.button("Unduh Skrip Sekarang"):
            download_repo()
            st.rerun()
    else:
        st.success("Direktori skrip 'easybux-master' sudah ada.")

    # Input dari pengguna yang biasanya ditanyakan oleh skrip
    user_agent = st.text_input(
        "User Agent", 
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    )
    cookie = st.text_area("Cookie", help="Masukkan cookie Anda di sini.")

    if st.button("🚀 Jalankan Bot"):
        if not cookie:
            st.warning("Harap masukkan cookie Anda.")
        elif not os.path.exists(os.path.join(script_dir, 'bot.php')):
             st.error("File 'bot.php' tidak ditemukan. Coba unduh ulang skrip.")
        else:
            with col2:
                st.header("📝 Log Eksekusi")
                st.info("Mencoba menjalankan skrip 'bot.php'...")
                
                # Membuat file config.php yang diperlukan oleh bot.php
                config_content = f"""<?php
$user_agent = "{user_agent}";
$cookie = "{cookie}";
?>"""
                try:
                    with open(os.path.join(script_dir, "config.php"), "w") as f:
                        f.write(config_content)
                    st.write("File 'config.php' berhasil dibuat.")

                    # Menjalankan skrip PHP menggunakan subprocess
                    process = subprocess.Popen(
                        ["php", os.path.join(script_dir, "bot.php")],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True,
                        bufsize=1,
                        universal_newlines=True
                    )

                    # Menampilkan output secara real-time
                    output_placeholder = st.empty()
                    log_output = ""
                    for line in iter(process.stdout.readline, ''):
                        log_output += line
                        # Membersihkan karakter aneh yang mungkin ada di output
                        cleaned_line = ''.join(filter(str.isprintable, line))
                        output_placeholder.code(log_output, language="bash")
                        time.sleep(0.05) # Sedikit jeda agar UI tidak freeze
                    
                    process.stdout.close()
                    stderr_output = process.stderr.read()
                    
                    if stderr_output:
                        st.error("Terjadi error saat eksekusi:")
                        st.code(stderr_output, language="bash")
                    else:
                        st.success("Eksekusi skrip selesai.")

                except FileNotFoundError:
                    st.error("Perintah 'php' tidak ditemukan.")
                    st.warning(
                        "Pastikan PHP terinstal di lingkungan tempat Anda menjalankan Streamlit. "
                        "Jika menggunakan Streamlit Cloud, Anda mungkin perlu menambahkan 'php' ke file 'packages.txt' Anda."
                    )
                except Exception as e:
                    st.error(f"Terjadi kesalahan yang tidak terduga: {e}")


with col2:
    st.header("💡 Cara Penggunaan & Tips")
    st.markdown("""
    1.  **Unduh Skrip**: Jika direktori skrip belum ada, klik tombol "Unduh Skrip Sekarang". Ini akan mengunduh dan mengekstrak kode dari GitHub.
    2.  **Masukkan User Agent**: User Agent adalah identitas browser Anda. Sebaiknya gunakan User Agent dari browser yang Anda pakai sehari-hari untuk mengurangi kecurigaan.
    3.  **Masukkan Cookie**: Ini adalah bagian terpenting. Anda harus mendapatkan nilai cookie dari sesi login Anda di situs EasyBux.
        * Login ke akun EasyBux Anda di browser.
        * Buka *Developer Tools* (biasanya dengan menekan F12).
        * Pergi ke tab `Application` (atau `Storage` di Firefox).
        * Cari bagian `Cookies` dan temukan cookie yang relevan untuk situs tersebut. Salin nilainya.
    4.  **Jalankan Bot**: Klik tombol "Jalankan Bot" dan lihat output yang muncul di area "Log Eksekusi".

    **Penting Mengenai Deteksi Bot:**
    * **Cookie adalah Kunci**: Jika cookie Anda tidak valid atau kedaluwarsa, skrip pasti gagal.
    * **User Agent**: Menggunakan User Agent yang umum dan valid sangat membantu.
    * **Alamat IP**: Jika Anda menjalankan ini dari server (seperti Streamlit Cloud), alamat IP Anda akan berasal dari pusat data (misalnya, Google atau AWS). Beberapa situs memblokir IP dari pusat data. Jika skrip gagal terhubung, ini bisa menjadi alasannya.
    * **Frekuensi Permintaan**: Skrip ini kemungkinan akan membuat permintaan secara cepat. Jika terlalu cepat, situs target bisa memblokir Anda untuk sementara. Sayangnya, memodifikasi jeda waktu memerlukan pengubahan pada kode `bot.php` itu sendiri.
    """)
