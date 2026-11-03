import os

# =========================================================
# KONFIGURASI & DATA
# =========================================================
TARIF = 1444.7

USERS = [
    ["admin", "admin123", "admin"],
    ["kiki", "kiki123", "user"]
]

DATA_LISTRIK = [
    [1, "Lampu", 10, 5, "12-10-2026"],
    [2, "Kipas Angin", 50, 8, "12-10-2026"],
    [3, "Kulkas", 100, 24, "12-10-2026"]
]

PENGAJUAN = []

# =========================================================
# UTIL & VALIDASI
# =========================================================
def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def format_durasi(durasi):
    return int(durasi) if float(durasi) == int(durasi) else durasi

def validasi_tanggal(tanggal):
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

def validasi_nama(nama):
    nama = nama.strip()
    if nama == "":
        raise ValueError("Nama perangkat tidak boleh kosong")
    return nama

def validasi_daya(daya):
    try:
        nilai = int(daya)
    except (ValueError, TypeError):
        raise ValueError("Daya harus angka")

    if nilai <= 0:
        raise ValueError("Daya harus lebih dari 0")

    return nilai

def validasi_durasi(durasi):
    try:
        nilai = float(durasi)
    except (ValueError, TypeError):
        raise ValueError("Durasi harus angka")

    if nilai <= 0:
        raise ValueError("Durasi harus lebih dari 0")

    if nilai > 24:
        raise ValueError("Durasi sehari tidak mungkin lebih dari 24 jam")

    return nilai

# =========================================================
# KALKULASI
# =========================================================
def hitung_kwh(daya, durasi):
    return float(daya) * float(durasi) / 1000

def hitung_tagihan(kwh):
    return kwh * TARIF

def hitung_total_kwh_rekursif(data, index=0):
    if index == len(data):
        return 0
    kwh = hitung_kwh(data[index][2], data[index][3])
    return kwh + hitung_total_kwh_rekursif(data, index + 1)

def hitung_total_kwh(data):
    return hitung_total_kwh_rekursif(data)

# =========================================================
# HELPER ID & INDEX
# =========================================================
def get_id_listrik_baru():
    if len(DATA_LISTRIK) == 0:
        return 1
    return DATA_LISTRIK[-1][0] + 1

def get_id_pengajuan_baru():
    if len(PENGAJUAN) == 0:
        return 1
    return PENGAJUAN[-1][0] + 1

def cari_index_listrik(id_cari):
    for i in range(len(DATA_LISTRIK)):
        if DATA_LISTRIK[i][0] == id_cari:
            return i
    return -1

def cari_index_pengajuan(id_cari):
    for i in range(len(PENGAJUAN)):
        if PENGAJUAN[i][0] == id_cari:
            return i
    return -1
