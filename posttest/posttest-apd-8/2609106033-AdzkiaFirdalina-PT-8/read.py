from prettytable import PrettyTable
from colorama import Fore
import storage

def tampilkan_data_biling():
    storage.bersihkan_layar()
    print(Fore.CYAN + "=" * 70)
    print("            DAFTAR PENGGUNAAN LISTRIK")
    print("=" * 70 + Fore.RESET)
    if len(storage.DATA_LISTRIK) == 0:
        print(Fore.YELLOW + "Belum ada data" + Fore.RESET)
        input("Tekan Enter Untuk Melanjutkan...")
        return
    table = PrettyTable()
    table.field_names = ["ID", "Perangkat", "Daya (W)", "Durasi (jam)", "Tanggal", "kWh", "Biaya"]
    table.align["Perangkat"] = "l"
    total = storage.hitung_total_kwh(storage.DATA_LISTRIK)
    for d in storage.DATA_LISTRIK:
        kwh = storage.hitung_kwh(d[2], d[3])
        biaya = storage.hitung_tagihan(kwh)
        table.add_row([d[0], d[1], d[2], storage.format_durasi(d[3]), d[4], f"{kwh:.3f}", f"Rp {biaya:,.2f}"])
    table.add_row(["", "TOTAL", "", "", "", f"{total:.3f}", f"Rp {storage.hitung_tagihan(total):,.2f}"])
    print(table)
    input("Tekan Enter Untuk Melanjutkan...")

def tampilkan_daftar_user():
    storage.bersihkan_layar()
    print(Fore.CYAN + "=== DAFTAR USER ===" + Fore.RESET)
    table = PrettyTable()
    table.field_names = ["No", "Username", "Role"]
    table.align["Username"] = "l"
    for i, x in enumerate(storage.USERS, start=1):
        table.add_row([i, x[0], x[2]])
    print(table)
    input("Tekan Enter untuk melanjutkan...")

def tampilkan_total_penggunaan():
    storage.bersihkan_layar()
    print(Fore.CYAN + "=== TOTAL PENGGUNAAN ===" + Fore.RESET)
    if len(storage.DATA_LISTRIK) == 0:
        print(Fore.YELLOW + "Belum ada data" + Fore.RESET)
        input("Tekan Enter untuk melanjutkan...")
        return
    table = PrettyTable()
    table.field_names = ["Perangkat", "kWh", "Biaya"]
    table.align["Perangkat"] = "l"
    total = 0
    for d in storage.DATA_LISTRIK:
        kwh = storage.hitung_kwh(d[2], d[3])
        total += kwh
        table.add_row([d[1], f"{kwh:.3f}", f"Rp {storage.hitung_tagihan(kwh):,.2f}"])
    table.add_row(["TOTAL", f"{total:.3f}", f"Rp {storage.hitung_tagihan(total):,.2f}"])
    print(table)
    input("Tekan Enter untuk melanjutkan...")

def tampilkan_pengajuan():
    storage.bersihkan_layar()
    print(Fore.CYAN + "=== PENGAJUAN DARI USER ===" + Fore.RESET)
    if not storage.PENGAJUAN:
        print(Fore.YELLOW + "Belum ada pengajuan nih" + Fore.RESET)
        input("Tekan Enter Untuk Melanjutkan...")
        return False
    table = PrettyTable()
    table.field_names = ["ID", "User", "Perangkat", "Daya (W)", "Durasi (jam)", "Tanggal"]
    table.align["User"] = "l"
    table.align["Perangkat"] = "l"
    for p in storage.PENGAJUAN:
        table.add_row([p[0], p[1], p[2], p[3], storage.format_durasi(p[4]), p[5]])
    print(table)
    input("Tekan Enter untuk lanjut memproses...")
    return True

def tampilkan_total_user():
    storage.bersihkan_layar()
    print(Fore.CYAN + "=== TOTAL PENGGUNAAN ANDA ===" + Fore.RESET)
    total = storage.hitung_total_kwh(storage.DATA_LISTRIK)
    table = PrettyTable()
    table.field_names = ["Keterangan", "Nilai"]
    table.add_row(["Harian", f"{total:.3f} kWh"])
    table.add_row(["Biaya", f"Rp {storage.hitung_tagihan(total):,.2f}"])
    table.add_row(["Bulanan", f"Rp {storage.hitung_tagihan(total) * 30:,.2f}"])
    print(table)
    input("Tekan Enter...")
  
