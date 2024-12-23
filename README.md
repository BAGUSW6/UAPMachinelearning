# UAPMachinelearning

Bagus Wicaksono
2020110370311220

# Proyek Analisis Pemesanan Hotel

## Pendahuluan
Mengelola pemesanan hotel secara efektif adalah tantangan, terutama dengan tingginya tingkat pembatalan yang dapat menyebabkan kerugian finansial dan inefisiensi operasional. Proyek ini bertujuan untuk menganalisis data historis pemesanan hotel guna mengungkap faktor-faktor yang memengaruhi pembatalan, mengidentifikasi pola, dan memberikan wawasan yang dapat diimplementasikan untuk mengoptimalkan operasional hotel.

Proyek ini terdiri dari dua komponen utama:
- **File Markdown**: Gambaran umum tentang proyek dan tujuannya.
- **Notebook Jupyter**: Analisis data dan visualisasi secara mendetail.

---

## Deskripsi Data
Dataset mencakup informasi yang kaya tentang pemesanan hotel, seperti:
- **Demografi pelanggan**: Negara asal, segmen pasar.
- **Detail pemesanan**: Durasi menginap, tipe kamar, waktu tunggu (lead time).
- **Hasil pemesanan**: Status pembatalan.

**Fitur Utama Dataset:**
- **Variabel**: Lebih dari 10 fitur yang memberikan wawasan beragam.
- **Data Hilang**: Ditangani selama proses pembersihan.
- **Rentang Waktu**: Mencakup pemesanan selama beberapa tahun untuk analisis tren.

---

## Alur Analisis
1. **Pernyataan Masalah**: Mengurangi tingkat pembatalan dan mengoptimalkan okupansi hotel.
2. **Impor & Pembersihan Data**:
   - Menangani data yang hilang.
   - Memformat kolom agar konsisten (misalnya, tanggal, kategori).
3. **Analisis Data Eksploratif (EDA)**:
   - Memahami demografi pelanggan.
   - Menemukan tren dalam pemesanan dan pembatalan.
   - Menganalisis tren temporal (misalnya, musiman).
4. **Wawasan**:
   - Memberikan wawasan yang dapat ditindaklanjuti untuk pengambilan keputusan.
5. **Visualisasi**:
   - Menyoroti temuan dengan grafik dan plot yang menarik.

---

## Sorotan Pembersihan Data
1. **Data Hilang**:
   - Baris kritis dihapus (misalnya, status pembatalan yang hilang).
   - Nilai yang tidak kritis diimputasi jika memungkinkan.
2. **Memformat Kolom**:
   - Mengonversi kolom tanggal ke format datetime.
   - Standarisasi nilai kategori (misalnya, tipe kamar).
3. **Deteksi Outlier**:
   - Menggunakan boxplot untuk mengidentifikasi dan menangani outlier.

---

## Temuan Utama
### Tren Pembatalan
- Waktu tunggu yang lebih panjang berkorelasi dengan tingkat pembatalan yang lebih tinggi.
- Pelanggan dari negara tertentu menunjukkan kecenderungan pembatalan yang lebih tinggi.

### Preferensi Kamar
- Tipe kamar tertentu sering mengalami overbook, menyebabkan ketidakpuasan.

### Wawasan Operasional
- Insentif untuk masa inap yang lebih lama dapat mengurangi pembatalan.

---

## Rekomendasi
1. **Segmentasi Pelanggan**:
   - Fokuskan upaya pemasaran pada wilayah dengan tingkat pembatalan lebih rendah.
2. **Penyesuaian Kebijakan**:
   - Terapkan kebijakan pembatalan yang lebih ketat untuk pemesanan dengan waktu tunggu panjang.
3. **Strategi Harga**:
   - Tawarkan diskon untuk masa inap yang lebih lama.
4. **Penyesuaian Operasional**:
   - Optimalkan inventaris kamar berdasarkan tren permintaan.

---

## Keterbatasan
- **Ruang Lingkup Data**: Analisis terbatas pada satu rantai hotel.
- **Variabel yang Tidak Diamati**: Faktor seperti kondisi ekonomi tidak termasuk.
- **Kualitas Data**: Asumsi dibuat selama proses pembersihan.

---

## Pekerjaan Mendatang
- Memperluas analisis ke beberapa rantai hotel.
- Mengintegrasikan sumber data eksternal (misalnya, indikator ekonomi).
- Membangun model prediktif untuk memperkirakan pembatalan.

---

## Cara Mereproduksi
1. Clone repositori ini.
2. Instal paket Python yang diperlukan:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
3. Buka dan jalankan Notebook Jupyter untuk menjelajahi analisis.

---

Terima kasih telah menjelajahi **Proyek Analisis Pemesanan Hotel**! Lihat notebook untuk wawasan dan visualisasi lebih detail.
