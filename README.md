# UAPMachinelearning
# Prediksi Depresi Mahasiswa

Proyek ini adalah aplikasi berbasis web yang memprediksi kemungkinan depresi mahasiswa berdasarkan berbagai faktor akademik dan gaya hidup. Aplikasi ini menggunakan model machine learning untuk memberikan hasil prediksi yang dapat digunakan sebagai langkah awal dalam memahami kondisi mental mahasiswa.

---

## 🎯 Deskripsi Proyek

Kesehatan mental mahasiswa adalah salah satu aspek penting yang perlu diperhatikan, terutama di tengah tekanan akademik dan gaya hidup yang sering kali tidak seimbang. Proyek ini bertujuan untuk:

- Memberikan alat sederhana untuk memprediksi risiko depresi.
- Mengedukasi pengguna tentang pentingnya menjaga kesehatan mental.
- Membandingkan performa model **Random Forest (RF)** dan **Feedforward Neural Network (FNN)** dalam melakukan prediksi.

Aplikasi ini dibangun menggunakan **Streamlit** untuk antarmuka web dan mengintegrasikan model machine learning yang telah dilatih.

---

## ⚙️ Langkah Instalasi

Ikuti langkah-langkah berikut untuk menginstal dan menjalankan aplikasi ini di komputer Anda:

### 1. Clone Repository
```bash
git clone <url-repository>
cd <folder-repository>
```

### 2. Buat Virtual Environment
```bash
python -m venv env
source env/bin/activate       # Untuk macOS/Linux
env\Scripts\activate          # Untuk Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
```bash
streamlit run app.py
```

Aplikasi akan terbuka di browser pada alamat: `http://localhost:8501`

---

## 🤓 Deskripsi Model

### 1. **Random Forest (RF)**
- Model Random Forest menggunakan algoritma ensemble berbasis pohon keputusan.
- **Keunggulan:**
  - Mampu menangani data yang kompleks.
  - Cepat untuk dilatih dan dievaluasi.
- **Parameter Utama:**
  - `n_estimators`: 100
  - `max_depth`: 10
  - `min_samples_split`: 2

### 2. **Feedforward Neural Network (FNN)**
- Model FNN adalah neural network sederhana dengan 2 hidden layer.
- **Struktur:**
  - **Layer Input:** 7 fitur input.
  - **Hidden Layer 1:** 128 neuron, aktivasi ReLU.
  - **Hidden Layer 2:** 64 neuron, aktivasi ReLU.
  - **Layer Output:** 1 neuron, aktivasi sigmoid.
- **Keunggulan:**
  - Dapat memodelkan hubungan non-linear antar fitur.

---

## 🔍 Hasil dan Analisis

### 1. Confusion Matrix
**Random Forest:**
![Confusion Matrix RF](path/to/rf_confusion_matrix.png)

**Feedforward Neural Network:**
![Confusion Matrix FNN](path/to/fnn_confusion_matrix.png)

### 2. Classification Report

#### Random Forest
| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.86      | 0.84   | 0.85     | 3281    |
| 1     | 0.84      | 0.86   | 0.85     | 3254    |
| **Accuracy**       |         |         | **0.85**     | 6535    |
| **Macro Avg**      | 0.85    | 0.85    | 0.85     | 6535    |
| **Weighted Avg**   | 0.85    | 0.85    | 0.85     | 6535    |

#### Feedforward Neural Network
| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.85      | 0.83   | 0.84     | 3281    |
| 1     | 0.83      | 0.85   | 0.84     | 3254    |
| **Accuracy**       |         |         | **0.84**     | 6535    |
| **Macro Avg**      | 0.84    | 0.84    | 0.84     | 6535    |
| **Weighted Avg**   | 0.84    | 0.84    | 0.84     | 6535    |

### 3. Learning Curve
![Learning Curve](path/to/learning_curve.png)

### 4. Feature Importance
![Feature Importance](path/to/feature_importance.png)

**Kesimpulan:**
- **Random Forest** menunjukkan akurasi yang sedikit lebih tinggi dibandingkan FNN.
- **FNN** memiliki kemampuan yang seimbang antara precision dan recall.
- **Feature importance** membantu memahami faktor utama yang memengaruhi prediksi.

---

## 🌐 Link Live Demo

Aplikasi web dapat diakses melalui tautan berikut:
[**Live Demo Aplikasi**](https://your-live-demo-link.com)

---

## 📂 Struktur Proyek

- `app.py` - Kode Streamlit untuk aplikasi web.
- `rf_model.pkl` - Model Random Forest yang telah dilatih.
- `fnn_model.h5` - Model Feedforward Neural Network yang telah dilatih.
- `scaler.pkl` - Scaler untuk standarisasi data.
- `requirements.txt` - Daftar dependencies.
- `README.md` - Dokumentasi proyek.

---

## 🙏 Kontribusi

Jika Anda ingin berkontribusi pada proyek ini:
1. Fork repository ini.
2. Lakukan perubahan pada branch baru.
3. Kirimkan pull request.

---

## 🛠️ Teknologi yang Digunakan

- **Python**: Untuk pemrosesan data dan machine learning.
- **Streamlit**: Untuk antarmuka web.
- **Scikit-learn**: Untuk model Random Forest.
- **TensorFlow/Keras**: Untuk model Feedforward Neural Network.
- **Matplotlib & Seaborn**: Untuk visualisasi data.

---

## 📢 Author
Bagus Wicaksono
2020110370311220
