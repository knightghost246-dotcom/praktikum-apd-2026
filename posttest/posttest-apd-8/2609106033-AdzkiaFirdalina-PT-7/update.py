from storage import (
    DATA_LISTRIK, cari_index_listrik, 
    validasi_nama, validasi_daya, validasi_durasi, validasi_tanggal, 
    format_durasi, bersihkan_layar
)

def ubah_data_listrik(posisi, nama, daya, durasi, tanggal):
    DATA_LISTRIK[posisi][1] = nama
    DATA_LISTRIK[posisi][2] = daya
    DATA_LISTRIK[posisi][3] = durasi
    DATA_LISTRIK[posisi][4] = tanggal

def ubah_data_admin():
    bersihkan_layar()
    print("=== UBAH DATA ===")

    for d in DATA_LISTRIK:
        print(f"{d[0]}. {d[1]} - {d[2]}W - {format_durasi(d[3])}j - {d[4]}")

    print("")
    idx_input = input("ID yang mau diubah (0 buat batal): ").strip()

    if idx_input == "0":
        print("Gajadi ubah")
        input("Tekan Enter untuk melanjutkan...")
        return

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

    nama = validasi_nama(nama)
    daya_int = validasi_daya(daya)
    durasi_float = validasi_durasi(durasi)
    validasi_tanggal(tanggal)

    ubah_data_listrik(posisi, nama, daya_int, durasi_float, tanggal)
    print("[+] Data udah diubah")
    input("Tekan Enter untuk melanjutkan...")
