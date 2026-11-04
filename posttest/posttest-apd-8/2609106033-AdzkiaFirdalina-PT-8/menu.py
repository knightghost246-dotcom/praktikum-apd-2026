from colorama import Fore

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
