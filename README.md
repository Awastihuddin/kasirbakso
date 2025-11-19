## 👤 Pembuat

**Nama Tim** 
**Mas Brian Sayang Silahkan Maju Kedepan Untuk Mengambil Sembako**

**Nama Proyek** — Aplikasi Kasir Bakso Idaman

**Anggota Tim** 
   - Hamzah Muhammad Ali
   - Muhammad Fatihuddin Fawwaz

---

## 🍜 Tentang Proyek

**Aplikasi Kasir Bakso Idaman** adalah program kasir sederhana berbasis **Python murni** (tanpa instalasi library tambahan) yang dibuat untuk membantu UMKM kecil dalam mencatat pesanan, menghitung total, menyimpan struk, dan mencetak struk dalam bentuk **file TXT** maupun **HTML siap-print**.

Proyek ini dibuat sebagai bagian dari pengembangan ide kompetisi, melalui proses iteratif antara user dan AI (ChatGPT) yang melibatkan perbaikan kode secara bertahap.

---

## 🎯 Fitur Utama

* ✔ **Menu bertingkat** (kategori → subkategori → item)
* ✔ **Tambah, kurangi, dan hapus pesanan**
* ✔ **Hitung total otomatis**
* ✔ **Struk TXT** (dengan timestamp unik)
* ✔ **Struk HTML** lengkap dengan auto-print (`window.print()`)
* ✔ **Tidak membutuhkan library eksternal**
* ✔ **Portable** (bekerja di Windows, Linux, macOS)

---

## 📂 Struktur Folder

```
proyek_kasir/
│
├── Bakso_Idaman.py   # file utama
├── struk/                                # folder otomatis untuk struk
│   ├── struk_12-30-00__21-11-2025.txt
│   ├── struk_12-30-00__21-11-2025.html
│   └── ...
└── README.md
```

---

## 🧾 Cara Menjalankan Program

1. Pastikan Python sudah terinstall (versi 3.8 atau lebih baru).
2. Jalankan program melalui terminal:

   ```bash
   python Bakso_Idaman.py
   ```
3. Ikuti instruksi di layar:

   * Tampilkan menu
   * Tambah pesanan
   * Kurangi pesanan
   * Hapus pesanan
   * Tampilkan pesanan
   * Cetak struk
4. Saat mencetak:

   * Struk TXT akan disimpan di folder `struk/`
   * Struk HTML otomatis terbuka di browser dan menampilkan dialog print

---

## 📦 Teknologi dan Modul yang Digunakan

Hanya modul bawaan Python:

| Modul            | Fungsi                                        |
| ---------------- | --------------------------------------------- |
| `os`             | membuat folder, path file                     |
| `datetime`       | timestamp struk                               |
| `pathlib`        | path portable (Windows/Linux/macOS)           |
| `webbrowser`     | membuka file HTML di browser                  |
| `builtins`       | input/output                                  |
| `encoding=utf-8` | memastikan teks struk tampil benar di browser |
| `time`           | menambahkan fungsi timeout waktu              |

**Tidak ada paket pip yang digunakan.**

---

## 🔧 Mekanisme Struk

### 📝 Struk TXT

Disimpan di folder `struk/` dengan format:

```
struk_12-30-05__21-11-2025.txt
```

Isi contoh:

```
=============Bakso Idaman==============
Bakso Urat - Rp 1500 x 2 = Rp 3000
Es Teh - Rp 3000 x 1 = Rp 3000
----------------------------------------
Total: Rp 6000
Terimakasih telah berbelanja!
```

---

### 🌐 Struk HTML

Dibuat dengan format yang rapi:

* Border
* Shadow
* Font bersih
* Auto print

Browser akan membuka file lalu otomatis menampilkan jendela print.

---

## 🧪 Proses Pengembangan (Ringkas)

Proyek ini melalui workflow iterasi:

1. Mulai dari konsep kasir sangat sederhana (hanya 1 item).
2. Ditambah kategori dan subkategori menu.
3. Dibuat fitur tambah/kurangi/hapus pesanan.
4. Implementasi struk TXT.
5. Versi menggunakan Flask (kemudian dibatalkan karena aturan lomba).
6. Revisi ke versi **non-Flask**, menggunakan `webbrowser`.
7. Perbaikan bug (cari harga, validasi input, path portable).
8. Membuat versi final yang stabil dan bebas library eksternal.

---

## ✅ Status Proyek

**Stabil / Final**
Siap digunakan sebagai proyek lomba, tugas sekolah, atau digunakan langsung oleh UMKM kecil.

---


