import storage
import read

def ubah_data_admin():
    storage.bersihkan_layar()
    print("=== UBAH DATA ===")
    for d in storage.DATA_LISTRIK:
        print(f"{d[0]}. {d[1]} - {d[2]}W - {storage.format_durasi(d[3])}j - {d[4]}")
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

    posisi = storage.cari_index_listrik(idx)
    if posisi == -1:
        raise ValueError("ID gak ketemu")

    nama = input("Nama baru    : ").strip()
    daya = input("Daya baru    : ").strip()
    durasi = input("Durasi baru  : ").strip()
    tanggal = input("Tanggal baru : ").strip()

    nama = storage.validasi_nama(nama)
    daya_int = storage.validasi_daya(daya)
    durasi_float = storage.validasi_durasi(durasi)
    storage.validasi_tanggal(tanggal)

    storage.ubah_data_listrik(posisi, nama, daya_int, durasi_float, tanggal)
    print("[+] Data udah diubah")
    input("Tekan Enter untuk melanjutkan...")

def proses_pengajuan_admin():
    if not read.tampilkan_pengajuan():
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

    posisi = storage.cari_index_pengajuan(id_pil)
    if posisi == -1:
        raise ValueError("ID pengajuan gak ketemu")

    print("")
    print(f"Pengajuan dari : {storage.PENGAJUAN[posisi][1]}")
    print(f"Perangkat      : {storage.PENGAJUAN[posisi][2]}")
    print(f"Daya           : {storage.PENGAJUAN[posisi][3]} W")
    print(f"Durasi         : {storage.format_durasi(storage.PENGAJUAN[posisi][4])} jam")
    print(f"Tanggal        : {storage.PENGAJUAN[posisi][5]}\n")

    aksi = input("Mau di-ACC atau ditolak? (acc/tolak): ").strip().lower()
    if aksi == "acc":
        dobel = False
        for d in storage.DATA_LISTRIK:
            if d[1].lower() == storage.PENGAJUAN[posisi][2].lower() and d[4] == storage.PENGAJUAN[posisi][5]:
                dobel = True
        if dobel:
            print("Perangkat ini udah ada di data biling")
        else:
            storage.tambah_data_listrik(storage.PENGAJUAN[posisi][2], storage.PENGAJUAN[posisi][3], storage.PENGAJUAN[posisi][4], storage.PENGAJUAN[posisi][5])
            storage.hapus_pengajuan(posisi)
            print("Pengajuan di-ACC, data udah masuk ke biling")
    elif aksi == "tolak":
        storage.hapus_pengajuan(posisi)
        print("Pengajuan ditolak")
    else:
        print("Pilihan gak ada, coba lagi")
    input("Tekan Enter Untuk Melanjutkan...")
  
