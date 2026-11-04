import sys
try:
    from prettytable import PrettyTable
    from colorama import Fore, init
except ImportError:
    print("[!] Library belum terinstall.")
    print("    Jalankan dulu: pip install prettytable colorama")
    sys.exit(1)

init(autoreset=True)

import storage
import autentikasi
import menu
import read
import create
import update
import delete

def main():
    while True:
        storage.bersihkan_layar()
        print("=" * 50)
        print("        WELCOME TO WATTWISE")
        print("   Monitor Ur Electricity Usage")
        print("=" * 50)

        username = input("Username : ").strip().lower()
        password = input("Password : ").strip().lower()

        if not autentikasi.username_terdaftar(username):
            print("")
            print(f"Username {username} anda belum terdaftar.")
            jawab = input("Registrasi sekarang? (y/n): ").strip().lower()

            if jawab == "y":
                try:
                    nu = input("Username baru : ").strip().lower()
                    np = input("Password baru : ").strip().lower()
                    nu = autentikasi.registrasi_user(nu, np)
                    print(f"Berhasil daftar! Silakan login pake username: {nu}")
                except ValueError as e:
                    print(f"Gagal registrasi: {e}")
                input("Tekan Enter untuk melanjutkan...")
            else:
                print("")
                print("Yaudah keluar dulu ya. Terima kasih!")
                break
            continue

        role = autentikasi.cek_login(username, password)

        if role is None:
            print("")
            print("Password salah!")
            input("Tekan Enter untuk melanjutkan...")
            continue

        print("")
        print(f"Login sebagai {role.upper()}. Halo, {username}!")
        input("Tekan Enter untuk melanjutkan...")

        while True:
            storage.bersihkan_layar()
            print("=" * 50)
            print(f"   MENU {role.upper()} - {username}")
            menu.tampilkan_menu(role)

            pilih = input("Pilih: ").strip()

            try:
                if pilih == "1":
                    read.tampilkan_data_biling()
                elif pilih == "2" and role == "admin":
                    create.tambah_data_admin()
                elif pilih == "3" and role == "admin":
                    update.ubah_data_admin()
                elif pilih == "4" and role == "admin":
                    delete.hapus_data_admin()
                elif pilih == "5" and role == "admin":
                    read.tampilkan_daftar_user()
                elif pilih == "6" and role == "admin":
                    read.tampilkan_total_penggunaan()
                elif pilih == "7" and role == "admin":
                    update.proses_pengajuan_admin()
                elif pilih == "2" and role == "user":
                    read.tampilkan_total_user()
                elif pilih == "3" and role == "user":
                    create.ajukan_perangkat(username)
                elif pilih == "0":
                    print("")
                    print("Yah, Logout dulu ya")
                    input("Tekan Enter untuk melanjutkan...")
                    break
                else:
                    print("Yhaaaa Pilihannya gak ada, silahkan coba lagi")
                    input("Tekan Enter untuk melanjutkan...")
            except ValueError as e:
                print(f"[!] Error: {e}")
                input("Tekan Enter untuk melanjutkan...")
            except Exception as e:
                print(f"[!] Terjadi kesalahan: {e}")
                input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
