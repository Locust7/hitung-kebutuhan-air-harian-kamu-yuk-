import streamlit as st
import random

# Konfigurasi halaman
st.set_page_config(page_title="💧 Kalkulator Kebutuhan Air Harian", layout="centered")

# Tambahkan latar belakang biru tua dengan gambar yang valid
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75)),
                    url('https://images.unsplash.com/photo-1532009324734-20a7a5813719?auto=format&fit=crop&w=1400&q=80');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""  
    <h1 style='text-align: center; color: #FFFF00;'>💧🐧 Kalkulator Kebutuhan Air Harian 🥤🍉</h1>
    <p style='text-align: center;'>Yuk hitung berapa banyak kamu harus minum biar nggak jadi kaktus! 🌵➡💦</p>
""", unsafe_allow_html=True)

# Penjelasan awal
st.markdown("""  
Kalkulator ini membantu kamu memperkirakan kebutuhan air harian berdasarkan:

- 🎂 *Umur*  
- 🚻 *Jenis kelamin*  
- ⚖ *Berat badan*  
- 🤸 *Aktivitas fisik*  
- ☀ *Iklim tempat tinggal*  

---

## 📚 Informasi Tentang Air dan Hidrasi 💧

**Kenapa Air Itu Penting?**  
Air adalah komponen utama tubuh manusia yang mendukung berbagai fungsi vital, seperti mengatur suhu tubuh, mendukung proses pencernaan, serta menjaga keseimbangan elektrolit. Tanpa cukup air, tubuh kita tidak dapat berfungsi dengan optimal.

**Manfaat Minum Air**:
1. **Meningkatkan Konsentrasi dan Fokus** 🧠  
2. **Membantu Pencernaan** 💪  
3. **Mengatur Suhu Tubuh** 🌡️  
4. **Mencegah Sakit Kepala** 🤕

""")

# Form input
with st.form("form_air"):
    umur = st.number_input("🎂 Umur (tahun)", min_value=0, max_value=120, value=25)
    jenis_kelamin = st.selectbox("🚻 Jenis Kelamin", ["👦 Laki-laki", "👧 Perempuan"])
    berat_badan = st.number_input("⚖ Berat Badan (kg)", min_value=1.0, max_value=200.0, value=60.0)

    aktivitas = st.selectbox("🤸 Tingkat Aktivitas Fisik", [
        "Ringan (pekerjaan ringan, sedikit olahraga) 🐌",
        "Sedang (olahraga 3–5 kali/minggu) 🏃‍♂️",
        "Berat (olahraga intens atau pekerjaan berat) 🏋️"
    ])

    iklim = st.selectbox("☀ Iklim Tempat Tinggal", [
        "Sedang/Dingin 🧣",
        "Panas (tropis, kering, atau sangat lembap) 🏖️"
    ])

    submitted = st.form_submit_button("🚰 Hitung Kebutuhan Air!")

# Proses perhitungan
if submitted:
    with st.spinner("⏳ Menghitung kebutuhan air harian kamu... 🕒"):

        kebutuhan_dasar_min = 30 * berat_badan / 1000
        kebutuhan_dasar_max = 40 * berat_badan / 1000

        faktor_aktivitas = 1.1 if aktivitas.startswith("Ringan") else 1.25 if aktivitas.startswith("Sedang") else 1.35
        faktor_iklim = 1.1 if iklim.startswith("Panas") else 1.0

        kebutuhan_total_min = kebutuhan_dasar_min * faktor_aktivitas * faktor_iklim
        kebutuhan_total_max = kebutuhan_dasar_max * faktor_aktivitas * faktor_iklim

        st.success("🎉 Perhitungan selesai! 🎉")
        st.subheader("💡 Hasil Perkiraan Kamu: 🥤")
        st.write(f"- 💧 Kebutuhan dasar: *{kebutuhan_dasar_min:.2f} - {kebutuhan_dasar_max:.2f} L/hari*")
        st.write(f"- 🔄 Setelah penyesuaian: *{kebutuhan_total_min:.2f} - {kebutuhan_total_max:.2f} L/hari*")

        st.markdown("""  
        <div style='background-color:#e6f7ff; padding:10px; border-left:5px solid #00BFFF;'>
            📌 <strong>Catatan:</strong><br>
            Nilai ini merupakan estimasi kebutuhan air harian. Kebutuhan sebenarnya bisa bervariasi tergantung kondisi kesehatan, konsumsi makanan dan minuman lain, serta cuaca harian. Konsultasikan dengan ahli gizi atau tenaga medis untuk kebutuhan spesifik.
        </div>
        """, unsafe_allow_html=True)

        reminder_frequency = st.slider("⏰ Pengingat Minum Air (dalam menit)", min_value=15, max_value=120, value=60, step=15)
        st.warning(f"⏰ Setiap {reminder_frequency} menit, kamu disarankan untuk minum air segelas! 🍶")

        st.subheader("🍽️ Rekomendasi Menu untuk Hidrasi yang Lebih Baik: 🥗🍉")
        st.markdown("""  
        - 🍉 **Buah-buahan**: Semangka, melon, dan jeruk kaya akan kandungan air!
        - 🥗 **Sayuran Hijau**: Selada, timun, dan bayam juga membantu tubuh tetap terhidrasi.
        - 🧃 **Minuman Sehat**: Teh herbal atau infused water dengan irisan lemon atau mentimun.
        - 🍶 **Air Kelapa**: Menyegarkan dan penuh elektrolit alami!
        """)

        st.info("🧊 Tips: Minumlah air secara bertahap sepanjang hari, jangan sekaligus kayak minum sirup waktu buka puasa! 😆")

        st.subheader("🩺 Tips Profesional dari Pakar Kesehatan: 💼")
        st.markdown("""  
        <div style='background-color:#fff8e1; padding:15px; border-left:5px solid #f4c430; border-radius:10px;'>
            <ul>
                <li>👩‍⚕️ <strong>Dr. Hydrina Segar</strong>: "Minumlah air sebelum merasa haus. 🌊"</li>
                <li>🧑‍⚕️ <strong>Dr. Aqua Vita</strong>: "Selalu bawa botol air ke mana pun kamu pergi. 🚶‍♂️💧"</li>
                <li>👨‍⚕️ <strong>Dr. Sehat Jernih</strong>: "Perhatikan warna urinmu. Urin gelap = kurang minum. 🔍🚽"</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.subheader("💡 Fun Fact tentang Air & Tubuhmu! 🤓")
        fakta_air = [
            "🧠 Otak manusia terdiri dari sekitar 75% air!",
            "💧 Kehilangan hanya 2% cairan tubuh bisa menurunkan fokus dan konsentrasi.",
            "🧃 Air membantu mengangkut nutrisi dan oksigen ke seluruh tubuh.",
            "🚽 Minum cukup air membantu ginjal menyaring limbah dengan lebih efektif.",
            "🔥 Air membantu mengatur suhu tubuh lewat keringat.",
            "😴 Minum cukup air bisa membantu kualitas tidurmu jadi lebih baik!",
            "👶 Bayi memiliki persentase air lebih tinggi daripada orang dewasa, hingga 78% dari berat tubuh!"
        ]
        st.info(random.choice(fakta_air))

# Watermark
st.markdown("""  
    <hr style="border: 1px solid #00BFFF;">
    <p style="text-align: center; font-size: 16px; color: grey;">
    🐬 Dibuat oleh <strong>LPK 7</strong> dengan cinta 💙:<br>
    <b>Daviona ✨, Ifta 🧋, Nadila 🎀, Vania 🌸, Sulthan 🎩</b><br>
    <i>Tim paling segar di antara deadline! 🍹</i>
    </p>
    <p style="text-align: center; font-size: 14px; color: grey;">
    <i>Design &amp; Development oleh Tim Kreatif LPK 7, 2025</i>
