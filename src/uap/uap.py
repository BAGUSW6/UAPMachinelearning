import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import joblib

# Load models dan scaler dengan pengecekan error
try:
    fnn_model = load_model('fnn_model.h5')
    rf_model = joblib.load('rf_model.pkl')
    scaler = joblib.load('scaler.pkl')
except Exception as e:
    st.error(f"Ups, ada masalah pas ngeload model atau scaler: {e}")
    st.stop()

# Judul Aplikasi
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🧠 Prediksi Depresi Mahasiswa</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Karena Kesehatan Mental itu Penting Banget!</h3>", unsafe_allow_html=True)
st.markdown("---")

# Penjelasan Singkat
st.write("""
    Hai, Sobat Gen Z! 👋 
    Kamu lagi galau atau penasaran sama kondisi mentalmu? Yuk, coba aplikasi ini buat cek kemungkinan 
    depresi kamu berdasarkan beberapa faktor. Tenang aja, ini cuma prediksi dan nggak akan nge-judge kok. 😊
""")

# Form Input di Halaman Utama
st.markdown("### 📚 Faktor Akademik")
academic_pressure = st.slider("Academic Pressure (0-5)", min_value=1, max_value=5, value=3)
study_satisfaction = st.slider("Study Satisfaction (0-5)", min_value=1, max_value=5, value=3)

st.markdown("### 🌟 Faktor Gaya Hidup")
financial_stress = st.slider("Financial Stress (1-5)", min_value=0, max_value=5, value=3)
work_study_hours = st.slider("Work/Study Hours per day", min_value=0, max_value=12, value=6)
dietary_habits = st.selectbox("Dietary Habits", ["Healthy", "Moderate", "Unhealthy"])
sleep_duration = st.selectbox("Sleep Duration", ["Less than 5 hours", "5-6 hours", "7-8 hours", "More than 8 hours"])
suicidal_thoughts = st.selectbox("Have you ever had suicidal thoughts?", ["Yes", "No"])

# Siapkan Data Input dengan Nama Kolom yang Sama dengan Model
input_data = pd.DataFrame({
    "Have you ever had suicidal thoughts ?": [1 if suicidal_thoughts == "Yes" else 0],
    "Academic Pressure": [academic_pressure],
    "Financial Stress": [financial_stress],
    "Work/Study Hours": [work_study_hours],
    "Dietary Habits": [1 if dietary_habits == "Healthy" else 2 if dietary_habits == "Moderate" else 3],
    "Study Satisfaction": [study_satisfaction],
    "Sleep Duration": [1 if sleep_duration == "Less than 5 hours" else 2 if sleep_duration == "5-6 hours" else 3 if sleep_duration == "7-8 hours" else 4],
})

# Urutkan Kolom Sesuai Model
expected_features = [
    "Have you ever had suicidal thoughts ?", 
    "Academic Pressure", 
    "Financial Stress", 
    "Work/Study Hours", 
    "Dietary Habits", 
    "Study Satisfaction", 
    "Sleep Duration"
]
try:
    input_data = input_data[expected_features]
except KeyError as e:
    st.error(f"Ups, ada masalah sama input datanya: {e}")
    st.stop()

# Standardisasi Data
try:
    input_data = scaler.transform(input_data)
except Exception as e:
    st.error(f"Ada error pas scaling: {e}")
    st.stop()

# Prediksi
if st.button("Prediksi Sekarang 🚀"):
    try:
        # Prediksi FNN
        fnn_prediction = fnn_model.predict(input_data)
        fnn_result = "Risiko Tinggi" if fnn_prediction[0][0] > 0.5 else "Risiko Rendah"

        # Prediksi RF
        rf_prediction = rf_model.predict(input_data)
        rf_result = "Risiko Tinggi" if rf_prediction[0] == 1 else "Risiko Rendah"

        # Tampilkan Hasil
        st.markdown("### Hasil Prediksi 💡")
        st.success(f"**Prediksi FNN:** {fnn_result}")
        st.info(f"**Prediksi RF:** {rf_result}")

        # Motivasi Berdasarkan Prediksi
        if fnn_result == "Risiko Tinggi" or rf_result == "Risiko Tinggi":
            st.warning("Kamu nggak sendiri, Sob. Kalau merasa berat, coba cerita ke orang terpercaya atau cari bantuan profesional. 💪")
        else:
            st.success("Mantap, Sob! Kamu lagi baik-baik aja. Tetap jaga kesehatan mental dan terus semangat! 💚")

        # Visualisasi Input
        st.markdown("---")
        st.markdown("### Visualisasi Data Input 📊")
        st.bar_chart(pd.DataFrame({
            "Faktor": ["Academic Pressure", "Study Satisfaction", "Financial Stress", "Work/Study Hours"],
            "Nilai": [academic_pressure, study_satisfaction, financial_stress, work_study_hours]
        }).set_index("Faktor"))

    except Exception as e:
        st.error(f"Ups, ada masalah pas prediksi: {e}")
