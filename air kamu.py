import streamlit as st
from datetime import datetime
import random

# DETEKSI SIANG/MALAM
current_hour = datetime.now().hour
bg_image = (
    "https://images.unsplash.com/photo-1589467235304-46069d5a3a4a"
    if 6 <= current_hour <= 18
    else "https://images.unsplash.com/photo-1505483531331-fc3cf89fd382"
)

# KONFIGURASI HALAMAN
st.set_page_config(page_title="💧 Kalkulator Kebutuhan Air Lucu", layout="centered")
st.markdown(f"""
<style>
.stApp {{
    background-image: url('{bg_image}?ixlib=rb-4.0.3&auto=format&fit=crop&w=1650&q=80');
    background-size: cover;
    background-attachment: fixed;
}}
.block-container {{
    background-color: rgba(255, 255, 255, 0.90);
    padding: 2rem;
    border-radius: 15px;
}}
</style>
""", unsafe_allow_html=True)

# JUDUL
st.markdown("""
    <h1 style='text-align: center; color: #00BFFF;'>💧🐧 Kalkulator Kebutuhan Air Harian Lucu 🥤🍉</h1>
    <p style='text-align: center;'>Yuk hitung berapa banyak kamu harus minum biar nggak jadi kaktus! 🌵➡💦</p>
""", unsafe_allow_html=True)

# FORM INPUT
with st.form("form_air"):
    st.subheader("📋 Input Data Kamu")
    umur = st.number_input("🎂 Umur (tahun)", 0, 120, 25)
    jenis_kelamin = st.selectbox("🚻 Jenis Kelamin", ["👦 Laki-laki", "👧 Perempuan"])
    berat_badan = st.number_input("⚖ Berat Badan (kg)", 1.0, 200.0, 60.0)
    aktivitas = st.selectbox("🤸 Aktivitas Fisik", ["Ringan", "Sedang", "Berat"])
    iklim = st.selectbox("☀ Iklim Tempat Tinggal", ["Sedang/Dingin", "Panas"])
    intake_air = st.number_input("💧 Perkiraan Air yang Diminum Hari Ini (Liter)", 0.0, 10.0, 1.5)
    reminder = st.slider("⏰ Interval Pengingat Minum (menit)", 15, 120, 60, step=15)
    submitted = st.form_submit_button("🚰 Hitung Kebutuhan Air!")

# PROSES & OUTPUT
if submitted:
    faktor_akt = {"Ringan": 1.1, "Sedang": 1.25, "Berat": 1.35}[aktivitas]
    faktor_iklim = 1.1 if iklim == "Panas" else 1.0
    dasar_min = 30 * berat_badan / 1000
    dasar_max = 40 * berat_badan / 1000
    total_min = dasar_min * faktor_akt * faktor_iklim
    total_max = dasar_max * faktor_akt * faktor_iklim

    st.success("🎉 Perhitungan selesai!")
    st.subheader("💡 Hasil Perkiraan Kamu:")
    st.write(f"- 💧 Kebutuhan dasar: *{dasar_min:.2f} - {dasar_max:.2f} L/hari*")
    st.write(f"- 🔄 Setelah penyesuaian: *{total_min:.2f} - {total_max:.2f} L/hari*")
    st.warning(f"⏰ Minum air setiap {reminder} menit ya biar tetap segar! 🍶")

    # SIMULASI DEHIDRASI
    if intake_air < total_min * 0.6:
        st.error("🚨 Potensi dehidrasi ringan! Gejala: pusing, lelah, mulut kering.")
    elif intake_air < total_min:
        st.warning("⚠️ Kamu kurang minum hari ini. Tambahkan asupan airmu!")
    else:
        st.success("✅ Kamu cukup minum air hari ini. Good job! 💙")

    # MENU HIDRASI
    st.subheader("🍽️ Rekomendasi Makanan & Minuman:")
    st.markdown("""
    - 🍉 **Buah Segar**: Semangka, melon, jeruk.
    - 🥗 **Sayur Kaya Air**: Selada, timun, bayam.
    - 🧃 **Minuman Sehat**: Infused water, teh herbal.
    - 🥥 **Air Kelapa**: Elektrolit alami!
    """)

    # FUN FACT
    st.subheader("💡 Fun Fact Tentang Air")
    st.info(random.choice([
        "🧠 Otakmu terdiri dari 75% air!",
        "🔥 Air bantu atur suhu tubuh lewat keringat.",
        "🚽 Cukup minum bantu ginjal bersihkan tubuh.",
        "😴 Kurang minum bisa ganggu kualitas tidur!"
    ]))

# FOOTER
st.markdown("""
<hr>
<p style='text-align: center; font-size: 16px; color: grey;'>
🐬 Dibuat oleh <strong>LPK 7</strong> dengan cinta 💙<br>
<b>Daviona ✨, Ifta 🧋, Nadila 🎀, Vania 🌸, Sulthan 🎩</b><br>
<i>Tim paling segar di antara deadline! 🍹</i>
</p>
""", unsafe_allow_html=True)

