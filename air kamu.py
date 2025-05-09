import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Konfigurasi halaman
st.set_page_config(page_title="💧 Kalkulator Kebutuhan Air Lucu", layout="centered")

# Tema siang/malam
tema = st.toggle("🌗 Mode Gelap / Terang", value=False)
if tema:
    latar_warna = "#222"
    teks_warna = "#eee"
    kotak_warna = "rgba(255,255,255,0.1)"
else:
    latar_warna = "#f0f8ff"
    teks_warna = "#000"
    kotak_warna = "rgba(255,255,255,0.9)"

# Latar belakang & gaya
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {latar_warna};
    }}
    .block-container {{
        background-color: {kotak_warna};
        padding: 2rem;
        border-radius: 15px;
    }}
    h1, h2, h3, h4, h5, h6, p, label {{
        color: {teks_warna};
    }}
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <h1 style='text-align: center;'>💧🐧 Kalkulator Kebutuhan Air Harian Lucu 🥤🍉</h1>
    <p style='text-align: center;'>Yuk hitung berapa banyak kamu harus minum biar nggak jadi kaktus! 🌵➡💦</p>
""", unsafe_allow_html=True)

# Penjelasan
st.markdown("""
Kalkulator ini membantu kamu memperkirakan kebutuhan air harian berdasarkan:
- 🎂 *Umur*
- 🚻 *Jenis kelamin*
- ⚖ *Berat badan*
- 🤸 *Aktivitas fisik*
- ☀ *Iklim tempat tinggal*
""")

# Form input
with st.form("form_air"):
    umur = st.number_input("🎂 Umur (tahun)", min_value=0, max_value=120, value=25)
    jenis_kelamin = st.selectbox("🚻 Jenis Kelamin", ["👦 Laki-laki", "👧 Perempuan"])
    berat_badan = st.number_input("⚖ Berat Badan (kg)", min_value=1.0, max_value=200.0, value=60.0)

    aktivitas = st.selectbox("🤸 Tingkat Aktivitas Fisik", [
        "Ringan (pekerjaan ringan, sedikit olahraga)",
        "Sedang (olahraga 3–5 kali/minggu)",
        "Berat (olahraga intens atau pekerjaan berat)"
    ])

    iklim = st.selectbox("☀ Iklim Tempat Tinggal", [
        "Sedang/Dingin",
        "Panas (tropis, kering, atau sangat lembap)"
    ])

    submitted = st.form_submit_button("🚰 Hitung Kebutuhan Air!")

if submitted:
    with st.spinner("⏳ Menghitung kebutuhan air harian kamu..."):
        # Dasar
        kebutuhan_dasar_min = 30 * berat_badan / 1000
        kebutuhan_dasar_max = 40 * berat_badan / 1000

        # Aktivitas
        faktor_aktivitas = 1.1 if aktivitas.startswith("Ringan") else 1.25 if aktivitas.startswith("Sedang") else 1.35

        # Iklim
        faktor_iklim = 1.1 if iklim.startswith("Panas") else 1.0

        # Total
        kebutuhan_total_min = kebutuhan_dasar_min * faktor_aktivitas * faktor_iklim
        kebutuhan_total_max = kebutuhan_dasar_max * faktor_aktivitas * faktor_iklim

        st.success("🎉 Perhitungan selesai!")
        st.subheader("💡 Hasil Perkiraan Kamu:")
        st.write(f"- 💧 Kebutuhan dasar: *{kebutuhan_dasar_min:.2f} - {kebutuhan_dasar_max:.2f} L/hari*")
        st.write(f"- 🔄 Setelah penyesuaian: *{kebutuhan_total_min:.2f} - {kebutuhan_total_max:.2f} L/hari*")

        st.markdown("""
        <div style='background-color:#e6f7ff; padding:10px; border-left:5px solid #00BFFF;'>
            📌 <strong>Catatan:</strong><br>
            Ini hanya estimasi. Konsultasikan dengan ahli gizi atau dokter untuk info lebih lanjut.
        </div>
        """, unsafe_allow_html=True)

        # Grafik kebutuhan air
        st.subheader("📊 Visualisasi Kebutuhan Air Berdasarkan Aktivitas")
        aktivitas_labels = ['Ringan', 'Sedang', 'Berat']
        faktor_aktivitas_list = [1.1, 1.25, 1.35]
        kebutuhan_min = [kebutuhan_dasar_min * f * faktor_iklim for f in faktor_aktivitas_list]
        kebutuhan_max = [kebutuhan_dasar_max * f * faktor_iklim for f in faktor_aktivitas_list]

        x = np.arange(len(aktivitas_labels))
        width = 0.35
        fig, ax = plt.subplots()
        ax.bar(x - width/2, kebutuhan_min, width, label='Min (L)')
        ax.bar(x + width/2, kebutuhan_max, width, label='Max (L)')

        ax.set_ylabel('Liter per Hari')
        ax.set_title('Perkiraan Kebutuhan Air vs Aktivitas')
        ax.set_xticks(x)
        ax.set_xticklabels(aktivitas_labels)
        ax.legend()
        ax.grid(axis='y', linestyle='--', alpha=0.6)
        st.pyplot(fig)

        # Reminder
        reminder_frequency = st.slider("⏰ Pengingat Minum Air (dalam menit)", min_value=15, max_value=120, value=60, step=15)
        st.warning(f"⏰ Setiap {reminder_frequency} menit, kamu disarankan untuk minum air segelas! 🍶")

        # Menu Hidrasi
        st.subheader("🍽️ Rekomendasi Menu Hidrasi:")
        st.markdown("""
        - 🍉 Semangka, melon, jeruk
        - 🥗 Timun, selada, bayam
        - 🧃 Infused water, teh herbal
        - 🥥 Air kelapa segar
        """)

        # Streak harian (pakai session_state)
        st.subheader("🔥 Streak Minum Air")
        if "streak" not in st.session_state:
            st.session_state.streak = 0
        tambah = st.button("✅ Saya sudah minum cukup hari ini!")
        if tambah:
            st.session_state.streak += 1
        st.info(f"📅 Kamu sudah konsisten selama {st.session_state.streak} hari berturut-turut! Keep going! 💪💧")

        # Kuis Hidrasi
        st.subheader("💡 Kuis Hidrasi")
        kuis_answer = st.selectbox("Apa manfaat utama dari hidrasi yang cukup?", [
            "Mengatur suhu tubuh 🧊",
            "Meningkatkan konsentrasi 🧠",
            "Mencegah dehidrasi 🏜️"
        ])
        if kuis_answer == "Mencegah dehidrasi 🏜️":
            st.success("✅ Betul! Hidrasi membantu mencegah dehidrasi!")
        else:
            st.warning("🤔 Coba pikirkan kembali... Yang paling utama adalah mencegah dehidrasi!")

        # Tips lucu
        st.info("🧊 Tips: Minumlah air bertahap, jangan sekaligus kayak minum es sirup waktu buka! 😆")

        # Tips dari pakar
        st.subheader("🩺 Tips Profesional dari Pakar Kesehatan")
        st.markdown("""
        <div style='background-color:#fff8e1; padding:15px; border-left:5px solid #f4c430; border-radius:10px;'>
            <ul>
                <li>👩‍⚕️ <b>Dr. Hydrina Segar</b>: "Minumlah sebelum haus. Haus = tanda tubuh kekurangan cairan."</li>
                <li>🧑‍⚕️ <b>Dr. Aqua Vita</b>: "Bawa botol air ke mana pun kamu pergi!"</li>
                <li>👨‍⚕️ <b>Dr. Sehat Jernih</b>: "Cek warna urinmu! Semakin jernih, semakin baik."</li>
                <li>👩‍⚕️ <b>Dr. Minerva Airin</b>: "Penderita ginjal/jantung sebaiknya konsultasi dulu sebelum minum berlebih."</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Watermark
st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 16px;

