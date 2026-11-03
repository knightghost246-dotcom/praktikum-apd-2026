from colorama import Fore
from storage import (
    DATA_LISTRIK, PENGAJUAN, 
    cari_index_pengajuan, format_durasi, bersihkan_layar
)
from read import tampilkan_pengajuan
from create import tambah_data_listrik
from delete import hapus_pengajuan

def tampilkan_menu(role):
    print(Fore.CYAN + "=" * 50)
    if role == "admin":
        print("1. View Data Biling    4. Hapus Data Biling")
        print("2. Tambah Data Biling  5. Lihat Informasi User")
        print("3. Ubah Data Biling    6. Total Tagihan")
        print("7. Lihat Pengajuan User")
    else:
        print("1. View Data Biling")
        print("2. Total Konsumsi Saya")
        print("3. Ajukan Penambahan Perangkat")
    print("0. Logout")
    print("=" * 50 + Fore.RESET)

def proses_pengajuan_admin():
    ada = tampilkan_pengajuan()
    if not ada:
        return

    id_input = input("Masukkan ID pengajuan yang mau diproses (0 buat batal): ").strip()

    if id_input == "0":
        print("Gajadi proses")
        input("Tekan Enter Untuk Melanjutkan...")
        return

    try:
        id_pil = int(id_input)
    except ValueError:
        raise ValueError("ID harus angka")

    posisi = cari_index_pengajuan(id_pil)
    if posisi == -1:
        raise ValueError("ID pengajuan gak ketemu")

    print("")
    print(f"Pengajuan dari : {PENGAJUAN[posisi][1]}")
    print(f"Perangkat      : {PENGAJUAN[posisi][2]}")
    print(f"Daya           : {PENGAJUAN[posisi][3]} W")
    print(f"Durasi         : {format_durasi(PENGAJUAN[posisi][4])} jam")
    print(f"Tanggal        : {PENGAJUAN[posisi][5]}")
    print("")

    aksi = input("Mau di-ACC atau ditolak? (acc/tolak): ").strip().lower()

    if aksi == "acc":
        dobel = False
        for d in DATA_LISTRIK:
            if (d[1].lower() == PENGAJUAN[posisi][2].lower() and d[4] == PENGAJUAN[posisi][5]):
                dobel = True

        if dobel:
            print("Perangkat ini udah ada di data biling")
        else:
            tambah_data_listrik(
                PENGAJUAN[posisi][2], PENGAJUAN[posisi][3],
                PENGAJUAN[posisi][4], PENGAJUAN[posisi][5]
            )
            hapus_pengajuan(posisi)
            print("Pengajuan di-ACC, data udah masuk ke biling")

    elif aksi == "tolak":
        hapus_pengajuan(posisi)
        print("Pengajuan ditolak")
    else:
        print("Pilihan gak ada, coba lagi")

    input("Tekan Enter Untuk Melanjutkan...")
