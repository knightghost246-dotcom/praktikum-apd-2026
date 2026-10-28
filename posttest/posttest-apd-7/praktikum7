import os
import datetime

users = [
    ["admin", "admin123", "admin"],
    ["kiki",  "kiki123",  "user"]
]
data_listrik = [
    [1, "Lampu",       10,  5,  "12-10-2026"],
    [2, "Kipas Angin", 50,  8,  "12-10-2026"],
    [3, "Kulkas",      100, 24, "12-10-2026"]
]
pengajuan = []
TARIF = 1444.7


def cek_login(username, password):
    """Return role ('admin'/'user') jika cocok, None jika tidak."""
    try:
        for x in users:
            if x[0] == username and x[1] == password:
                return x[2]
        return None
    except (IndexError, TypeError):
        return None


def validasi_tanggal(tanggal):
    """Validasi format dd-mm-yyyy. Raise ValueError jika tidak valid."""
    bagian = tanggal.split("-")
    if len(bagian) != 3:
        raise ValueError("Format tanggal harus dd-mm-yyyy")
    try:
        dd = int(bagian[0])
        mm = int(bagian[1])
        yy = int(bagian[2])
    except ValueError:
        raise ValueError("Tanggal harus berisi angka semua")
    if dd < 1 or dd > 31 or mm < 1 or mm > 12 or yy < 2000:
        raise ValueError("Tanggal tidak valid")
    return True


def hitung_kwh(daya, durasi):
    """Return kWh = daya * durasi / 1000."""
    try:
        return float(daya) * float(durasi) / 1000
    except (ValueError, TypeError):
        raise ValueError("Daya dan durasi harus angka")


def hitung_tagihan(kwh):
    """Return rupiah = kwh * TARIF."""
    return kwh * TARIF


# =========================================================
# FUNGSI TANPA PARAMETER (3 — memenuhi ≥ 2)
# =========================================================
def get_id_listrik_baru():
    if len(data_listrik) == 0:
        return 1
    return data_listrik[-1][0] + 1


def get_id_pengajuan_baru():
    if len(pengajuan) == 0:
        return 1
    return pengajuan[-1][0] + 1


def hitung_total_kwh():
    """Wrapper tanpa parameter untuk fungsi rekursif."""
    return hitung_total_kwh_rekursif()


# =========================================================
# FUNGSI REKURSIF (wajib)
# =========================================================
def hitung_total_kwh_rekursif(index=0):
    """Jumlahkan kWh semua data_listrik secara rekursif."""
    if index == len(data_listrik):          # BASE CASE
        return 0
    kwh = hitung_kwh(data_listrik[index][2], data_listrik[index][3])
    return kwh + hitung_total_kwh_rekursif(index + 1)   # RECURSIVE


def cari_index_listrik(id_cari):
    """Return index data_listrik dengan id tertentu, atau -1."""
    for i in range(len(data_listrik)):
        if data_listrik[i][0] == id_cari:
            return i
    return -1


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def tampilkan_menu(role):
    print("=" * 50)
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
    print("=" * 50)


def tampilkan_data_biling():
    bersihkan_layar()
    print("=" * 70)
    print("            DAFTAR PENGGUNAAN LISTRIK")
    print("=" * 70)
    if len(data_listrik) == 0:
        print("Belum ada data")
    else:
        print("ID  Perangkat        Daya   Jam   Tanggal        kWh")
        print("-" * 70)
        for d in data_listrik:
            kwh = hitung_kwh(d[2], d[3])
            print(f"{d[0]}   {d[1]}   {d[2]}W   {d[3]}j   {d[4]}   {round(kwh, 3)}")
        total = hitung_total_kwh()
        print("-" * 70)
        print(f"TOTAL : {round(total, 3)} kWh  |  Rp {round(hitung_tagihan(total), 2)}")
    input("Tekan Enter Untuk Melanjutkan...")


def main():
    while True:
        bersihkan_layar()
        print("=" * 50)
        print("        WELCOME TO WATTWISE")
        print("   Monitor Ur Electricity Usage")
        print("=" * 50)
        username = input("Username : ").strip().lower()
        password = input("Password : ").strip().lower()

        user_ada = False
        for x in users:
            if x[0] == username:
                user_ada = True

        if user_ada == False:
            print("")
            print(f"Username {username} anda belum terdaftar.")
            jawab = input("Registrasi sekarang? (y/n): ")
            if jawab.lower() == "y":
                try:
                    nu = input("Username baru : ").strip().lower()
                    np = input("Password baru : ").strip().lower()
                    if nu == "":
                        raise ValueError("Username gak boleh kosong")
                    if np == "":
                        raise ValueError("Password gak boleh kosong")
                    if any(u[0] == nu for u in users):
                        raise ValueError("Username udah dipake, cari yang lain")
                    users.append([nu, np, "user"])
                    print(f"Berhasil daftar! Silakan login pake username: {nu}")
                except ValueError as e:
                    print(f"Gagal registrasi: {e}")
                input("Tekan Enter untuk melanjutkan...")
            else:
                print("")
                print("Yaudah keluar dulu ya. Terima kasih!")
                break
            continue

        role = cek_login(username, password)
        if role is None:
            print("")
            print("Password salah!")
            input("Tekan Enter untuk melanjutkan...")
            continue

        print("")
        print(f"Login sebagai {role.upper()}. Halo, {username}!")
        input("Tekan Enter untuk melanjutkan...")

        while True:
            bersihkan_layar()
            print("=" * 50)
            print(f"   MENU {role.upper()} - {username}")
            tampilkan_menu(role)
            pilih = input("Pilih: ")

            try:
                if pilih == "1":
                    tampilkan_data_biling()

                elif pilih == "2" and role == "admin":
                    bersihkan_layar()
                    print("=== TAMBAH DATA ===")
                    print("Ketik 0 di nama perangkat buat batal")
                    print("")
                    nama = input("Nama perangkat      : ").strip()
                    if nama == "0":
                        print("Gajadi nambah data")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                    daya = input("Daya (Watt)         : ").strip()
                    durasi = input("Durasi (jam)        : ").strip()
                    tanggal = input("Tanggal (dd-mm-yyyy): ").strip()

                    if nama == "":
                        raise ValueError("Namanya jangan dikosongin")
                    try:
                        daya_int = int(daya)
                    except ValueError:
                        raise ValueError("Daya harus angka")
                    if daya_int <= 0:
                        raise ValueError("Daya harus lebih dari 0")
                    try:
                        durasi_float = float(durasi)
                    except ValueError:
                        raise ValueError("Durasi harus angka")
                    if durasi_float <= 0:
                        raise ValueError("Durasi harus lebih dari 0")
                    if durasi_float > 24:
                        raise ValueError("Durasi sehari gak mungkin lebih dari 24 jam")
                    validasi_tanggal(tanggal)
                    for d in data_listrik:
                        if d[1].lower() == nama.lower() and d[4] == tanggal:
                            raise ValueError("Data ini udah ada")
                    id_baru = get_id_listrik_baru()
                    data_listrik.append([id_baru, nama, daya_int, durasi_float, tanggal])
                    print(f"[+] Data berhasil ditambah, ID nya {id_baru}")
                    input("Tekan Enter untuk melanjutkan...")

                elif pilih == "3" and role == "admin":
                    bersihkan_layar()
                    print("=== UBAH DATA ===")
                    for d in data_listrik:
                        print(f"{d[0]}. {d[1]} - {d[2]}W - {d[3]}j - {d[4]}")
                    print("")
                    idx_input = input("ID yang mau diubah (0 buat batal): ").strip()
                    if idx_input == "0":
                        print("Gajadi ubah")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                    try:
                        idx = int(idx_input)
                    except ValueError:
                        raise ValueError("ID harus angka")
                    posisi = cari_index_listrik(idx)
                    if posisi == -1:
                        raise ValueError("ID gak ketemu")
                    nama = input("Nama baru    : ").strip()
                    daya = input("Daya baru    : ").strip()
                    durasi = input("Durasi baru  : ").strip()
                    tanggal = input("Tanggal baru : ").strip()
                    if nama == "":
                        raise ValueError("Nama jangan kosong")
                    try:
                        daya_int = int(daya)
                    except ValueError:
                        raise ValueError("Daya harus angka")
                    if daya_int <= 0:
                        raise ValueError("Daya harus lebih dari 0")
                    try:
                        durasi_float = float(durasi)
                    except ValueError:
                        raise ValueError("Durasi harus angka")
                    if durasi_float <= 0:
                        raise ValueError("Durasi harus lebih dari 0")
                    if durasi_float > 24:
                        raise ValueError("Durasi sehari gak mungkin lebih dari 24 jam")
                    validasi_tanggal(tanggal)
                    data_listrik[posisi][1] = nama
                    data_listrik[posisi][2] = daya_int
                    data_listrik[posisi][3] = durasi_float
                    data_listrik[posisi][4] = tanggal
                    print("[+] Data udah diubah")
                    input("Tekan Enter untuk melanjutkan...")

                elif pilih == "4" and role == "admin":
                    bersihkan_layar()
                    print("=== HAPUS DATA ===")
                    for d in data_listrik:
                        print(f"{d[0]}. {d[1]} - {d[4]}")
                    print("")
                    idx_input = input("ID yang mau dihapus (0 buat batal): ").strip()
                    if idx_input == "0":
                        print("Gajadi hapus")
                        input("Tekan Enter untuk melanjutkan...")
                        continue
                    try:
                        idx = int(idx_input)
                    except ValueError:
                        raise ValueError("ID harus angka")
                    posisi = cari_index_listrik(idx)
                    if posisi == -1:
                        raise ValueError("Sayang banget ID mu gak ketemu")
                    tanya = input(f"Yakin mau hapus {data_listrik[posisi][1]}? (y/n): ").lower()
                    if tanya == "y":
                        data_listrik.pop(posisi)
                        print("[+] Data udah dihapus")
                    else:
                        print("Gajadi hapus")
                    input("Tekan Enter untuk melanjutkan...")

                elif pilih == "5" and role == "admin":
                    bersihkan_layar()
                    print("=== DAFTAR USER ===")
                    no = 1
                    for x in users:
                        print(f"{no}. {x[0]} - {x[2]}")
                        no += 1
                    input("Tekan Enter untuk melanjutkan...")

                elif pilih == "6" and role == "admin":
                    bersihkan_layar()
                    print("=== TOTAL PENGGUNAAN ===")
                    for d in data_listrik:
                        kwh = hitung_kwh(d[2], d[3])
                        print(f"- {d[1]} : {round(kwh, 3)} kWh  (Rp {round(hitung_tagihan(kwh), 2)})")
                    print("-" * 45)
                    total = hitung_total_kwh()
                    print(f"TOTAL : {round(total, 3)} kWh  |  Rp {round(hitung_tagihan(total), 2)}")
                    input("Tekan Enter untuk melanjutkan...")

                elif pilih == "7" and role == "admin":
                    bersihkan_layar()
                    print("=== PENGAJUAN DARI USER ===")
                    if len(pengajuan) == 0:
                        print("Belum ada pengajuan nih")
                    else:
                        print("ID  User        Perangkat        Daya   Jam   Tanggal")
                        print("-" * 65)
                        for p in pengajuan:
                            print(f"{p[0]}   {p[1]}   {p[2]}   {p[3]}W   {p[4]}j   {p[5]}")
                        print("-" * 65)
                        print("")
                        id_input = input("Masukkan ID pengajuan yang mau diproses (0 buat batal): ").strip()
                        if id_input == "0":
                            print("Gajadi proses")
                        else:
                            try:
                                id_pil = int(id_input)
                            except ValueError:
                                raise ValueError("ID harus angka")
                            posisi = -1
                            for i in range(len(pengajuan)):
                                if pengajuan[i][0] == id_pil:
                                    posisi = i
                            if posisi == -1:
                                raise ValueError("ID pengajuan gak ketemu")
                            print("")
                            print(f"Pengajuan dari : {pengajuan[posisi][1]}")
                            print(f"Perangkat      : {pengajuan[posisi][2]}")
                            print(f"Daya           : {pengajuan[posisi][3]} W")
                            print(f"Durasi         : {pengajuan[posisi][4]} jam")
                            print(f"Tanggal        : {pengajuan[posisi][5]}")
                            print("")
                            aksi = input("Mau di-ACC atau ditolak? (acc/tolak): ").lower()
                            if aksi == "acc":
                                dobel = False
                                for d in data_listrik:
                                    if d[1].lower() == pengajuan[posisi][2].lower() and d[4] == pengajuan[posisi][5]:
                                        dobel = True
                                if dobel:
                                    print("Perangkat ini udah ada di data biling")
                                else:
                                    id_baru = get_id_listrik_baru()
                                    data_listrik.append([
                                        id_baru,
                                        pengajuan[posisi][2],
                                        pengajuan[posisi][3],
                                        pengajuan[posisi][4],
                                        pengajuan[posisi][5]
                                    ])
                                    pengajuan.pop(posisi)
                                    print("Pengajuan di-ACC, data udah masuk ke biling")
                            elif aksi == "tolak":
                                pengajuan.pop(posisi)
                                print("Pengajuan ditolak")
                            else:
                                print("Pilihan gak ada, coba lagi")
                    input("Tekan Enter Untuk Melanjutkan...")

                elif pilih == "2" and role == "user":
                    bersihkan_layar()
                    print("=== TOTAL PENGGUNAAN ANDA ===")
                    total = hitung_total_kwh()
                    print(f"Harian  : {round(total, 3)} kWh")
                    print(f"Biaya   : Rp {round(hitung_tagihan(total), 2)}")
                    print(f"Bulanan : Rp {round(hitung_tagihan(total) * 30, 2)}")
                    input("Tekan Enter...")

                elif pilih == "3" and role == "user":
                    bersihkan_layar()
                    print("=== AJUKAN PENAMBAHAN PERANGKAT ===")
                    print("[i] Isi datanya, admin bakal tinjau dulu")
                    print("")
                    nama = input("Mau nambah perangkat apa? ").strip()
                    daya = input("Berapa watt? ").strip()
                    durasi = input("Berapa jam pemakaian per hari? ").strip()
                    hari_ini = datetime.date.today()
                    tanggal = f"{hari_ini.day}-{hari_ini.month}-{hari_ini.year}"

                    if nama == "":
                        raise ValueError("Nama perangkatnya jangan kosong")
                    try:
                        daya_int = int(daya)
                    except ValueError:
                        raise ValueError("Watt harus angka")
                    if daya_int <= 0:
                        raise ValueError("Watt harus lebih dari 0")
                    try:
                        durasi_float = float(durasi)
                    except ValueError:
                        raise ValueError("Jam harus angka")
                    if durasi_float <= 0:
                        raise ValueError("Jam harus lebih dari 0")
                    if durasi_float > 24:
                        raise ValueError("Sehari gak mungkin lebih dari 24 jam")
                    for d in data_listrik:
                        if d[1].lower() == nama.lower():
                            raise ValueError("Perangkat ini udah ada di data biling")
                    for p in pengajuan:
                        if p[2].lower() == nama.lower():
                            raise ValueError("Kamu udah pernah ngajuin perangkat ini")

                    id_peng = get_id_pengajuan_baru()
                    pengajuan.append([id_peng, username, nama, daya_int, durasi_float, tanggal])
                    print("")
                    print(" Pengajuan anda berhasil dikirim!")
                    print(f"    Perangkat : {nama}")
                    print(f"    Watt      : {daya} W")
                    print(f"    Jam       : {durasi} jam")
                    print(f"    Tanggal   : {tanggal}")
                    print("")
                    print("    Tunggu di ACC admin ya")
                    input("Tekan Enter untuk melanjutkan...")

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
