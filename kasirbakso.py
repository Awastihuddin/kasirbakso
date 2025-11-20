# NAMA TIM : MAS BRIAN SAYANG SILAHKAN MAJU KE DEPAN UNTUK MENGAMBIL SEMBAKO
# APLIKASI KASIR BAKSO IDAMAN (tanpa library pihak ketiga)
import os
from datetime import datetime
from pathlib import Path
import webbrowser
import time
import platform

STRUK_FOLDER = Path.cwd() / 'struk'
STRUK_FOLDER.mkdir(parents=True, exist_ok=True)

menu = {
    'Makanan': {
        'Bakso': {
            'Bakso Biasa': 1000, 'Bakso Urat': 1500, 'Bakso Besar': 2000, 'Bakso Puyuh': 2500, 'Bakso Rawit': 6000, 'Bakso Mercon': 7000, 'Bakso Keju': 7000, 'Bakso Beranak': 10000
            },
        'Mie Ayam': {
            'Mie Ayam Biasa': 5000, 'Mie Ayam Bakso': 8000, 'Mie Ayam Ceker': 8000, 'Mie Ayam Spesial': 11000, 'Mie Ayam Jumbo': 13000, 'Mie Ayam Extra Toping': 15000, 'Mie Level': 10000
            }
    },
    'Minuman': {
        'Air Mineral Biasa': 2000, 'Es Teh': 3000, 'Es Jeruk': 4000, 'Es Degan': 5000, 'Es Campur': 6000, 'Es Soda Gembira': 6500, 'Es Susu Coklat': 6000, 'Es Blewah': 7000
    },
    'Sampingan': {
        'Pangsit': 1000, 'Ceker': 3000, 'Lontong': 2500, 'Tahu': 2000, 'Sate Telur Puyuh': 3000, 'Tahu Bakso': 2500
    }
}

pesanan = {}

# ------------------ Helper functions ------------------

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def pilih_kategori():
    while True:
        try:
            print("\n--- Pilih Kategori ---")
            for i, kategori in enumerate(menu.keys(), 1):
                print(f"{i}. {kategori}")
            pilihan = int(input("Masukkan nomor kategori: "))
            if 1 <= pilihan <= len(menu):
                return list(menu.keys())[pilihan - 1]
            else:
                print("Nomor kategori tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")


def pilih_item(kategori):
    while True:
        try:
            print(f"\n--- Pilih Item di Kategori {kategori} ---")
            items = menu[kategori]
            # Jika items adalah dict dengan subkategori
            if isinstance(items, dict):
                item_list = list(items.keys())
                for i, item in enumerate(item_list, 1):
                    print(f"{i}. {item}")
                idx = int(input("Masukkan nomor pilihan: ")) - 1
                selected = item_list[idx]

                # jika selected memiliki subitem (mis: 'Bakso' -> dict of types)
                if isinstance(items[selected], dict):
                    subitem_list = list(items[selected].keys())
                    for i, subitem in enumerate(subitem_list, 1):
                        print(f"{i}. {subitem}")
                    subidx = int(input("Masukkan nomor pilihan: ")) - 1
                    return subitem_list[subidx]

                return selected
            else:
                # tidak mungkin pada struktur ini, tapi aman
                return None
        except (ValueError, IndexError):
            print("Input tidak valid. Harap masukkan angka yang sesuai.")


def tampilkan_menu():
    clear()
    print("\n--- Daftar Menu ---")
    for kategori, items in menu.items():
        print(f"\n{kategori}:")
        if isinstance(items, dict):
            for subkategori, subitems in items.items():
                if isinstance(subitems, dict):
                    print(f"  {subkategori}:")
                    for nama, harga in subitems.items():
                        print(f"    {nama} - Rp {harga}")
                else:
                    print(f"  {subkategori} - Rp {subitems}")


def cari_harga(nama):
    nama = nama.lower()
    for kategori, items in menu.items():
        if isinstance(items, dict):
            for subkategori, subitems in items.items():
                if isinstance(subitems, dict):
                    for item_nama, harga in subitems.items():
                        if item_nama.lower() == nama:
                            return harga
                else:
                    if subkategori.lower() == nama:
                        return subitems
    return None


def tambah_pesanan():
    clear()
    while True:
        kategori = pilih_kategori()
        item = pilih_item(kategori)
        if item:
            try:
                jumlah = int(input(f"Berapa banyak {item} yang ingin ditambah?: "))
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
                continue

            if jumlah <= 0:
                print("Jumlah harus lebih dari 0. Silakan coba lagi.")
                continue
            harga = cari_harga(item)
            if harga is not None:
                pesanan[item] = pesanan.get(item, {'harga': harga, 'jumlah': 0})
                pesanan[item]['jumlah'] += jumlah
                print(f"{item} berhasil ditambahkan!")
                time.sleep(0.8)
                clear()
                break
            else:
                print("Item tidak ditemukan di menu!")
                time.sleep(0.8)
                clear()


def hapus_pesanan():
    clear()
    if not pesanan:
        print("\nBelum ada pesanan untuk dihapus.")
        time.sleep(1)
        clear()
        return

    tampilkan_pesanan()
    try:
        pilihan = int(input("Masukkan nomor pesanan yang ingin dihapus: ")) - 1
        item_list = list(pesanan.keys())
        if 0 <= pilihan < len(item_list):
            removed = item_list[pilihan]
            del pesanan[removed]
            print(f"Pesanan '{removed}' berhasil dihapus!")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
    time.sleep(1)
    clear()


def kurangi_pesanan():
    clear()
    if not pesanan:
        print("\nBelum ada pesanan untuk dikurangi.")
        time.sleep(1)
        clear()
        return

    tampilkan_pesanan()
    try:
        pilihan = int(input("Masukkan nomor pesanan yang ingin dikurangi: ")) - 1
        item_list = list(pesanan.keys())
        if pilihan < 0 or pilihan >= len(item_list):
            print("Nomor pesanan tidak valid. Silakan coba lagi.")
            time.sleep(1)
            clear()
            return
        item = item_list[pilihan]
        jumlah = int(input(f"Masukkan jumlah {item} yang ingin dikurangi: "))

        if jumlah < pesanan[item]['jumlah']:
            pesanan[item]['jumlah'] -= jumlah
            print(f"Jumlah {item} berhasil dikurangi!")
        elif jumlah == pesanan[item]['jumlah']:
            del pesanan[item]
            print(f"{item} dihapus dari pesanan.")
        else:
            print(f"Jumlah yang ingin dikurangi melebihi jumlah {item} dalam pesanan.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
    time.sleep(1)
    clear()


def tampilkan_pesanan():
    print("\n--- Pesanan Anda ---")
    if not pesanan:
        print("\nBelum Ada Pesanan")
    else:
        total_harga = sum(info['harga'] * info['jumlah'] for info in pesanan.values())
        for index, (nama, info) in enumerate(pesanan.items(), 1):
            total = info['harga'] * info['jumlah']
            print(f"{index}. {nama} (x{info['jumlah']}) - Rp {info['harga']} -> Rp {total}")
        print(f"\nTotal Harga: Rp {total_harga}")


def tampilkan_struk_keluar():
    struk = "\n=============Bakso Idaman==============\n"
    struk += "========================================\n"
    total_harga = 0
    if not pesanan:
        struk += "Belum Ada Pesanan\n"
    else:
        for item, details in pesanan.items():
            subtotal = details['harga'] * details['jumlah']
            struk += f"{item} - Rp {details['harga']} x {details['jumlah']} = Rp {subtotal}\n"
            total_harga += subtotal
        struk += "========================================\n"
        struk += f"Total: Rp {total_harga}\n"
    struk += "========================================\n"
    struk += "Terimakasih sudah berbelanja di Bakso Idaman\n"
    print(struk)
    return struk


# Fungsi untuk menyimpan struk sebagai .txt
def simpan_struk():
    try:
        timestamp = datetime.now().strftime("%H-%M-%S__%d-%m-%Y")
        filename = f"struk_{timestamp}.txt"
        path_file = STRUK_FOLDER / filename

        struk = tampilkan_struk_keluar()
        with open(path_file, "w", encoding="utf-8") as file:
            file.write(struk)

        print(f"Struk berhasil disimpan di: {path_file}")
        return path_file
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan struk: {e}")
        return None


# Fungsi untuk membuat file HTML struk dan membuka di browser (tanpa server eksternal)
def generate_html_file():
    timestamp = datetime.now().strftime("%H-%M-%S__%d-%m-%Y")
    filename = f"struk_{timestamp}.html"
    path_file = STRUK_FOLDER / filename

    total_harga = 0
    lines = []
    for item, details in pesanan.items():
        subtotal = details['harga'] * details['jumlah']
        lines.append(f"<p>{details['jumlah']} x {item} - Rp {details['harga']} = Rp {subtotal}</p>")
        total_harga += subtotal

    html_content = f"""
    <!doctype html>
    <html>
    <head>
      <meta charset="utf-8"> 
      <title>Struk Pesanan</title>
      <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .content {{ max-width: 600px; margin: auto; border: 1px solid #ccc; padding: 20px; border-radius: 10px; }}
        h1 {{ text-align: center; }}
        .total {{ font-weight: bold; text-align: right; margin-top: 20px; }}
      </style>
      <script>
        window.onload = function() {{ window.print(); }}
      </script>
    </head>
    <body>
      <div class="content">
        <h1>Struk Pesanan - Bakso Idaman</h1>
        {''.join(lines)}
        <p class="total">Total: Rp {total_harga}</p>
        <p style="text-align:center;">Terima kasih telah berbelanja di Bakso Idaman</p>
      </div>
    </body>
    </html>
    """

    try:
        with open(path_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Struk HTML dibuat: {path_file}")
        # Buka file HTML di browser default (file:// URL)
        webbrowser.open(path_file.resolve().as_uri())
        return path_file
    except Exception as e:
        print(f"Gagal membuat file HTML: {e}")
        return None


def print_exit_message(txt_filename=None, html_filename=None):
    if txt_filename:
        print(f"\nStruk disimpan sebagai {txt_filename}.")
    if html_filename:
        print(f"Struk HTML disimpan sebagai {html_filename} dan dibuka di browser untuk dicetak.")
    print("Terimakasih Telah Menggunakan Program Kasir Bakso Idaman")


def struk_cetak():
    clear()
    """
    Menampilkan struk, menanyakan pencetakan, menyimpan struk, lalu
    *mengosongkan pesanan* agar transaksi berikutnya dimulai dari kosong.
    """
    tampilkan_struk_keluar()
    pilihan = input("\nApakah Anda ingin mencetak struk? (y/n): ").strip().lower()
    if pilihan == 'y':
        txt_path = simpan_struk()
        html_path = generate_html_file()
        print_exit_message(txt_path.name if txt_path else None, html_path.name if html_path else None)
    elif pilihan == 'n':
        txt_path = simpan_struk()
        print_exit_message(txt_path.name if txt_path else None, None)
    else:
        print("Pilihan Anda Tidak Valid, Silahkan Coba Lagi!!!")
        time.sleep(1)
        clear()
        return struk_cetak()
    pesanan.clear()
    print("\nPesanan telah dikosongkan. Anda bisa membuat pesanan baru.\n")
    time.sleep(1)
    clear()


def kasir():
    clear()
    while True:
        tampilkan_pesanan()
        pilihan = input(
            "\n--- Aplikasi Kasir Tukang Bakso ---\n"
            "1. Tampilkan Menu\n"
            "2. Tambah Pesanan\n"
            "3. Kurangi Pesanan\n"
            "4. Hapus Pesanan\n"
            "5. Selesaikan Pesanan\n"
            "6. Keluar Tanpa Belanja\n"
            "Pilih menu (1/2/3/4/5/6): ").strip()

        if pilihan == '1':
            tampilkan_menu()
            input("\nTekan Enter untuk kembali...")
            clear()

        elif pilihan == '2':
            tambah_pesanan()

        elif pilihan == '3':
            kurangi_pesanan()

        elif pilihan == '4':
            hapus_pesanan()

        elif pilihan == '5':
            struk_cetak()
            while True:
                pilih = input("Apakah anda ingin membuat pesanan lain? (y/n): ").strip().lower()
                if pilih == 'y':
                    clear()
                    break  
                elif pilih == 'n':
                    print("Terimakasih sudah menggunakan Program Kasir Bakso Idaman, Semoga harimu menyenangkan :D")
                    time.sleep(3)
                    os._exit(0)
                else:
                    print("Pilihan Anda Tidak Valid, Silahkan Coba Lagi!!!")
                    continue

        elif pilihan == '6':
            print("Terimakasih sudah menggunakan Program Kasir Bakso Idaman, Semoga harimu menyenangkan :D")
            time.sleep(3)
            os._exit(0)

        else:
            print("Pilihan Anda Tidak Valid, Silahkan Coba Lagi!!!")
            time.sleep(3)
            clear()


if __name__ == "__main__":
    kasir()
