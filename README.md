# ✨ Prediksi Depresi Mahasiswa: Analisis Faktor Akademik dan Gaya Hidup dengan RF dan FNN ✨

## Table of Contents
1. [Overview Project](#-overview-project)
2. [Deskripsi Dataset](#-deskripsi-dataset)
3. [Preprocessing & Modelling](#-preprocessing--modelling)
   - [Random Forest Model](#-random-forest-model-)
   - [Feedforward Neural Network Model](#-feedforward-neural-network-model-)
   - [Learning Curve](#-learning-curve)
   - [Feature Importance](#-feature-importance)
4. [Local Web Deployment](#-local-web-deployment)
5. [Kesimpulan](#-kesimpulan)
6. [Author](#-author)

---

## 🔍 Overview Project
Proyek ini bertujuan untuk mengembangkan sebuah sistem prediksi risiko depresi pada mahasiswa berdasarkan faktor akademik dan gaya hidup. Sistem ini mengintegrasikan model machine learning **Random Forest** (RF) dan **Feedforward Neural Network** (FNN) untuk memberikan hasil prediksi yang akurat dan dapat dijadikan referensi awal.

---

## 📊 Deskripsi Dataset
Dataset yang digunakan mencakup data mahasiswa dengan atribut seperti tekanan akademik, stres keuangan, kebiasaan makan, durasi tidur, dan lainnya. Fitur-fitur ini membantu model dalam menentukan prediksi risiko depresi.

Dataset terdiri atas **6.535 data** yang telah diproses, dengan pembagian sebagai berikut:
- 70% sebagai *Training Set*
- 15% sebagai *Validation Set*
- 15% sebagai *Testing Set*

---

## 🔧 Preprocessing & Modelling

### ☀ Random Forest Model ✨
**Preprocessing**

- Standarisasi fitur numerik menggunakan **StandardScaler**.
- Mengatasi data tidak seimbang dengan **SMOTE** untuk oversampling kelas minoritas.

**Modelling**

Model Random Forest dilatih dengan parameter utama berikut:
- `n_estimators`: 100
- `max_depth`: 10
- `min_samples_split`: 2
- `min_samples_leaf`: 1

Hasil dari RF Model setelah evaluasi ditunjukkan dalam Confusion Matrix berikut:

![Confusion Matrix RF](path/to/rf_confusion_matrix.png)

**Model Evaluation**

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.86      | 0.84   | 0.85     | 3281    |
| 1     | 0.84      | 0.86   | 0.85     | 3254    |
| **Accuracy**       |         |         | **0.85**     | 6535    |
| **Macro Avg**      | 0.85    | 0.85    | 0.85     | 6535    |
| **Weighted Avg**   | 0.85    | 0.85    | 0.85     | 6535    |

### ☀ Feedforward Neural Network Model ✨
**Preprocessing**

- Standarisasi fitur numerik dengan **StandardScaler**.
- Pembagian dataset ke dalam *Training*, *Validation*, dan *Testing*.

**Modelling**

FNN dibangun dengan arsitektur berikut:
- **Input Layer**: 7 fitur input.
- **Hidden Layer 1**: 128 neuron, aktivasi ReLU.
- **Hidden Layer 2**: 64 neuron, aktivasi ReLU.
- **Output Layer**: 1 neuron, aktivasi sigmoid.

Hasil dari FNN Model setelah evaluasi ditunjukkan dalam Confusion Matrix berikut:

![Confusion Matrix FNN](path/to/fnn_confusion_matrix.png)

**Model Evaluation**

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 0.85      | 0.83   | 0.84     | 3281    |
| 1     | 0.83      | 0.85   | 0.84     | 3254    |
| **Accuracy**       |         |         | **0.84**     | 6535    |
| **Macro Avg**      | 0.84    | 0.84    | 0.84     | 6535    |
| **Weighted Avg**   | 0.84    | 0.84    | 0.84     | 6535    |

### 🔄 Learning Curve

**Random Forest**:
![Learning Curve RF](path/to/rf_learning_curve.png)

**Feedforward Neural Network**:
![Learning Curve FNN](path/to/fnn_learning_curve.png)

### 🔬 Feature Importance

Feature importance dari model Random Forest:
![Feature Importance](path/to/feature_importance.png)

---

## 🔐 Local Web Deployment

### Tampilan Aplikasi

- **Halaman Utama**:
![Homepage](path/to/homepage.png)

- **Hasil Prediksi**:
![Prediction Result](path/to/prediction_result.png)

---

## 🕵️‍♂️ Kesimpulan

- **Random Forest** menunjukkan akurasi sedikit lebih tinggi dibanding FNN, tetapi kedua model memiliki performa yang kompetitif.
- **Feature importance** membantu memahami faktor utama yang memengaruhi prediksi.
- Proyek ini dapat dikembangkan lebih lanjut dengan memperkaya dataset dan menambahkan fitur interpretasi hasil prediksi.

---

## 👨‍💻 Author 

- [Your Name](https://github.com/your-profile)

