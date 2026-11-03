from prettytable import PrettyTable
from colorama import Fore
from storage import (
    DATA_LISTRIK, PENGAJUAN, USERS, 
    hitung_kwh, hitung_tagihan, hitung_total_kwh, 
    format_durasi, bersihkan_layar
)

def tampilkan_data_biling():
    bersihkan_layar()
    print(Fore.CYAN + "=" * 70)
    print("            DAFTAR PENGGUNAAN LISTRIK")
    print("=" * 70 + Fore.RESET)

    if len(DATA_LISTRIK) == 0:
        print(Fore.YELLOW + "Belum ada data" + Fore.RESET)
        input("Tekan Enter Untuk Melanjutkan...")
        return

    table = PrettyTable()
    table.field_names = ["ID", "Perangkat", "Daya (W)", "Durasi (jam)", "Tanggal", "kWh", "Biaya"]
    table.align["Perangkat"] = "l"

    total = hitung_total_kwh(DATA_LISTRIK)

    for d in DATA_LISTRIK:
        kwh = hitung_kwh(d[2], d[3])
        biaya = hitung_tagihan(kwh)
        table.add_row([d[0], d[1], d[2], format_durasi(d[3]), d[4], f"{kwh:.3f}", f"Rp {biaya:,.2f}"])

    total_biaya = hitung_tagihan(total)
    table.add_row(["", "TOTAL", "", "", "", f"{total:.3f}", f"Rp {total_biaya:,.2f}"])

    print(table)
    input("Tekan Enter Untuk Melanjutkan...")

def tampilkan_daftar_user():
    bersihkan_layar()
    print(Fore.CYAN + "=== DAFTAR USER ===" + Fore.RESET)

    table = PrettyTable()
    table.field_names = ["No", "Username", "Role"]
    table.align["Username"] = "l"

    for i, x in enumerate(USERS, start=1):
        table.add_row([i, x[0], x[2]])

    print(table)
    input("Tekan Enter untuk melanjutkan...")

def tampilkan_total_penggunaan():
    bersihkan_layar()
    print(Fore.CYAN + "=== TOTAL PENGGUNAAN ===" + Fore.RESET)

    if len(DATA_LISTRIK) == 0:
        print(Fore.YELLOW + "Belum ada data" + Fore.RESET)
        input("Tekan Enter untuk melanjutkan...")
        return

    table = PrettyTable()
    table.field_names = ["Perangkat", "kWh", "Biaya"]
    table.align["Perangkat"] = "l"

    total = 0
    for d in DATA_LISTRIK:
        kwh = hitung_kwh(d[2], d[3])
        total += kwh
        table.add_row([d[1], f"{kwh:.3f}", f"Rp {hitung_tagihan(kwh):,.2f}"])

    table.add_row(["TOTAL", f"{total:.3f}", f"Rp {hitung_tagihan(total):,.2f}"])

    print(table)
    input("Tekan Enter untuk melanjutkan...")

def tampilkan_pengajuan():
    """Tampilkan tabel pengajuan. Return True jika ada data."""
    bersihkan_layar()
    print(Fore.CYAN + "=== PENGAJUAN DARI USER ===" + Fore.RESET)

    if not PENGAJUAN:
        print(Fore.YELLOW + "Belum ada pengajuan nih" + Fore.RESET)
        input("Tekan Enter Untuk Melanjutkan...")
        return False

    table = PrettyTable()
    table.field_names = ["ID", "User", "Perangkat", "Daya (W)", "Durasi (jam)", "Tanggal"]
    table.align["User"] = "l"
    table.align["Perangkat"] = "l"

    for p in PENGAJUAN:
        table.add_row([p[0], p[1], p[2], p[3], format_durasi(p[4]), p[5]])

    print(table)
    input("Tekan Enter untuk lanjut memproses...")
    return True

def tampilkan_total_user():
    bersihkan_layar()
    print(Fore.CYAN + "=== TOTAL PENGGUNAAN ANDA ===" + Fore.RESET)

    total = hitung_total_kwh(DATA_LISTRIK)

    table = PrettyTable()
    table.field_names = ["Keterangan", "Nilai"]
    table.add_row(["Harian", f"{total:.3f} kWh"])
    table.add_row(["Biaya", f"Rp {hitung_tagihan(total):,.2f}"])
    table.add_row(["Bulanan", f"Rp {hitung_tagihan(total) * 30:,.2f}"])

    print(table)
    input("Tekan Enter...")
