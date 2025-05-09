import streamlit as st
import time
import datetime
import matplotlib.pyplot as plt
import numpy as np

# Konfigurasi halaman
st.set_page_config(page_title="💧 Kalkulator Kebutuhan Air Lucu", layout="centered")

# Tambahkan latar belakang
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('https://images.unsplash.com/photo-1589467235304-46069d5a3a4a?ixlib=rb-4.0.3&auto=format&fit=crop&w=1650&q=80');
        background-size: cover;
        background-attachment: fixed;
    }}
    .block-container {{
        background-color: rgba(255, 255, 255, 0.90);
        padding: 2rem;
        border-radius: 15px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown("""
    <h1 style='text-align: center; color: #00BFFF;'>💧🐧 Kalkulator Kebutuhan Air Harian Lucu 🥤🍉</h1>
    <p style='text-align: center;'>Yuk hitung berapa banyak kamu harus minum biar nggak jadi kaktus! 🌵➡💦</p>
""", unsafe_allow_html=True)

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

        # Grafik visualisasi
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
        ax.set_title('Kebutuhan Air vs Aktivitas')
        ax.set_xticks(x)
        ax.set_xticklabels(aktivitas_labels)
        ax.legend()
        ax.grid(axis='y', linestyle='--', alpha=0.6)
        st.pyplot(fig)

        # 🎯 Tujuan harian & progress
        st.subheader("🎯 Target Hidrasi Hari Ini")
        target = st.slider("Tentukan target harian kamu (L)", min_value=1.0, max_value=5.0, value=2.0, step=0.1)
        minum = st.number_input("Berapa liter yang sudah kamu minum hari ini?", min_value=0.0, max_value=5.0, step=0.1)
        progress = min(minum / target, 1.0)
        st.progress(progress, text=f"{minum:.1f} L dari {target:.1f} L")

        # 🔔 Pengingat teks sederhana
        st.subheader("🔔 Simulasi Pengingat Minum Air")
        interval = st.selectbox("Setel interval pengingat", ["Setiap 30 menit", "Setiap 1 jam", "Setiap 2 jam"])
        st.info(f"📌 Ingat ya! Minum segelas air {interval.lower()}! Kamu bisa setel pengingat di HP juga! 📱💧")

        # 🗓️ Kalender catatan hidrasi
        st.subheader("🗓️ Catatan Hidrasi Harian")
        tanggal = st.date_input("Tanggal hari ini", datetime.date.today())
        catatan = st.text_input("Catatan hidrasi (opsional)", "")
        if catatan:
            st.success(f"📘 Catatan tersimpan untuk {tanggal}: {catatan}")

        # Tips
        st.subheader("🩺 Tips Profesional dari Pakar Kesehatan")
        st.markdown("""
        <div style='background-color:#fff8e1; padding:15px; border-left:5px solid #f4c430; border-radius:10px;'>
            <ul>
                <li>👩‍⚕️ <b>Dr. Hydrina Segar</b>: "Minumlah sebelum haus."</li>
                <li>🧑‍⚕️ <b>Dr. Aqua Vita</b>: "Selalu bawa botol air!"</li>
                <li>👨‍⚕️ <b>Dr. Sehat Jernih</b>: "Warna urin = indikator hidrasi."</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Watermark
st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 16px; color: grey;'>
    🐬 Dibuat oleh <strong>LPK 7</strong> dengan cinta 💙:<br>
    <b>Daviona ✨, Ifta 🧋, Nadila 🎀, Vania 🌸, Sulthan 🎩</b><br>
    <i>Tim paling segar di antara deadline! 🍹</i>
    </p>""", unsafe_allow_html=True)
