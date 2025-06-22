# ====================================================================================
# PENTING: CARA MEMPERBAIKI ERROR "ModuleNotFoundError: No module named 'selenium'"
# ====================================================================================
#
# Error ini terjadi karena server Streamlit tidak tahu pustaka apa saja yang 
# dibutuhkan oleh aplikasi Anda. Solusinya BUKAN dengan mengubah kode Python ini, 
# tetapi dengan membuat file konfigurasi di repositori GitHub Anda.
#
# Ikuti 3 langkah berikut dengan TEPAT:
#
# --- LANGKAH 1: Buat file bernama "requirements.txt" ---
# Pastikan file ini ada di repositori GitHub Anda, di lokasi yang sama dengan app.py.
# Isi dari file requirements.txt HARUS SAMA PERSIS seperti di bawah ini:
#
# streamlit
# selenium
# webdriver-manager
# 2captcha-python
#
#
# --- LANGKAH 2: Buat file bernama "packages.txt" ---
# File ini juga harus ada di repositori GitHub Anda.
# Isi dari file packages.txt HARUS SAMA PERSIS seperti di bawah ini:
#
# google-chrome-stable
#
#
# --- LANGKAH 3: Reboot Aplikasi Anda ---
# Setelah menyimpan kedua file di atas ke GitHub, buka aplikasi Anda di Streamlit
# Cloud, klik "Manage app" di pojok kanan bawah, dan pilih "Reboot".
#
# Setelah di-reboot, Streamlit akan menginstal semua yang dibutuhkan dan error akan hilang.
# ====================================================================================

import streamlit as st
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from twocaptcha import TwoCaptcha

# --- Tampilan Awal dan Konfigurasi ---
st.set_page_config(page_title="Advanced EasyBux Bot", layout="wide")

st.title("🤖 Advanced EasyBux Bot (dengan Selenium & Captcha Solver)")
st.warning("Aplikasi ini menggunakan teknologi canggih dan memerlukan API Key dari layanan penyelesai captcha seperti 2Captcha.", icon="⚠️")

# --- Fungsi-fungsi Utama ---

def solve_hcaptcha(api_key, site_key, page_url):
    """
    Fungsi untuk mengirim tantangan hCaptcha ke layanan 2Captcha dan mendapatkan solusinya.
    """
    st.info("Captcha terdeteksi. Mengirim ke layanan 2Captcha...")
    try:
        solver = TwoCaptcha(api_key)
        result = solver.hcaptcha(
            sitekey=site_key,
            url=page_url,
        )
        st.success("Captcha berhasil diselesaikan oleh layanan!")
        return result['code']
    except Exception as e:
        st.error(f"Gagal menyelesaikan captcha: {e}")
        return None

@st.cache_resource
def get_driver():
    """
    Menyiapkan driver Selenium Chrome untuk dijalankan di lingkungan server (headless).
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# --- Antarmuka Pengguna ---

st.sidebar.header("⚙️ Konfigurasi Bot")
twocaptcha_api_key = st.sidebar.text_input("1. 2Captcha API Key", type="password", help="Dapatkan API Key dari dasbor akun 2Captcha Anda.")
cookie_value = st.sidebar.text_input("2. Cookie PHPSESSID", help="Nilai cookie PHPSESSID setelah Anda login di easybux.net.")
run_button = st.sidebar.button("🚀 Mulai Proses Klaim Otomatis", use_container_width=True)

log_placeholder = st.empty()
log_messages = []

def log(message, level="info"):
    """Fungsi untuk menampilkan pesan log di UI."""
    log_messages.append(message)
    log_placeholder.code("\n".join(log_messages[::-1]), language="log")


if run_button:
    if not twocaptcha_api_key or not cookie_value:
        st.sidebar.error("Harap isi API Key dan Cookie terlebih dahulu.")
    else:
        log_messages.clear()
        driver = None
        try:
            log("Memulai proses bot...")
            driver = get_driver()
            log("Driver Selenium berhasil diinisialisasi.")
            
            log("Membuka situs target: https://easybux.net/")
            driver.get("https://easybux.net/")
            
            log("Menambahkan cookie login (PHPSESSID)...")
            driver.add_cookie({
                'name': 'PHPSESSID',
                'value': cookie_value,
                'domain': '.easybux.net'
            })
            log("Cookie berhasil ditambahkan.")

            faucet_url = "https://easybux.net/faucet"
            log(f"Navigasi ke halaman Faucet: {faucet_url}")
            driver.get(faucet_url)
            time.sleep(3)

            wait = WebDriverWait(driver, 20)
            claim_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Claim')]")))
            log("Tombol 'Claim' ditemukan.")
            claim_button.click()
            log("Tombol 'Claim' diklik.")
            time.sleep(5)

            log("Mencari iframe hCaptcha...")
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@src, 'hcaptcha.com')]")))
            log("Berhasil masuk ke dalam iframe captcha.")
            
            hcaptcha_element = wait.until(EC.presence_of_element_located((By.ID, "h-captcha")))
            site_key = hcaptcha_element.get_attribute("data-sitekey")
            
            if not site_key:
                raise Exception("Tidak dapat menemukan data-sitekey hCaptcha.")

            log(f"Site-key ditemukan: {site_key[:10]}...")
            driver.switch_to.default_content()

            captcha_solution = solve_hcaptcha(twocaptcha_api_key, site_key, faucet_url)

            if captcha_solution:
                log("Memasukkan token solusi captcha ke halaman...")
                driver.execute_script(
                    f"document.getElementsByName('h-captcha-response')[0].value = '{captcha_solution}';"
                )
                driver.execute_script(
                    f"document.getElementsByName('g-recaptcha-response')[0].value = '{captcha_solution}';"
                )
                log("Token berhasil dimasukkan.")
                time.sleep(2)

                verify_button = wait.until(EC.element_to_be_clickable((By.ID, "verifyCaptcha")))
                log("Tombol verifikasi ditemukan.")
                verify_button.click()
                log("Tombol verifikasi diklik. Menunggu hasil...")
                time.sleep(5)

                page_source = driver.page_source
                if "has been added to your balance" in page_source:
                    log("🎉 KLAIM BERHASIL! Saldo telah ditambahkan.", level="success")
                    st.balloons()
                else:
                    log("🔴 Klaim mungkin gagal. Silakan cek halaman untuk pesan error.", level="error")
            else:
                log("Proses berhenti karena captcha tidak dapat diselesaikan.", level="error")

        except Exception as e:
            log(f"Terjadi error fatal: {e}", level="error")
        finally:
            if driver:
                driver.quit()
                log("Driver Selenium telah ditutup.")
