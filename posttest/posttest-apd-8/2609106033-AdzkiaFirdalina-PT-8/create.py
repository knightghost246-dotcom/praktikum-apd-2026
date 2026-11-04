import datetime
import storage

def tambah_data_admin():
    storage.bersihkan_layar()
    print("=== TAMBAH DATA ===")
    print("Ketik 0 di nama perangkat buat batal\n")
    nama = input("Nama perangkat      : ").strip()
    if nama == "0":
        print("Gajadi nambah data")
        input("Tekan Enter untuk melanjutkan...")
        return
    daya = input("Daya (Watt)         : ").strip()
    durasi = input("Durasi (jam)        : ").strip()
    tanggal = input("Tanggal (dd-mm-yyyy): ").strip()

    nama = storage.validasi_nama(nama)
    daya_int = storage.validasi_daya(daya)
    durasi_float = storage.validasi_durasi(durasi)
    storage.validasi_tanggal(tanggal)

    for d in storage.DATA_LISTRIK:
        if d[1].lower() == nama.lower() and d[4] == tanggal:
            raise ValueError("Data ini udah ada")

    id_baru = storage.tambah_data_listrik(nama, daya_int, durasi_float, tanggal)
    print(f"[+] Data berhasil ditambah, ID nya {id_baru}")
    input("Tekan Enter untuk melanjutkan...")

def ajukan_perangkat(username):
    storage.bersihkan_layar()
    print("=== AJUKAN PENAMBAHAN PERANGKAT ===")
    print("[i] Isi datanya, admin bakal tinjau dulu\n")
    nama = input("Mau nambah perangkat apa? ").strip()
    daya = input("Berapa watt? ").strip()
    durasi = input("Berapa jam pemakaian per hari? ").strip()
    hari_ini = datetime.date.today()
    tanggal = f"{hari_ini.day:02d}-{hari_ini.month:02d}-{hari_ini.year}"

    nama = storage.validasi_nama(nama)
    daya_int = storage.validasi_daya(daya)
    durasi_float = storage.validasi_durasi(durasi)

    for d in storage.DATA_LISTRIK:
        if d[1].lower() == nama.lower():
            raise ValueError("Perangkat ini udah ada di data biling")
    for p in storage.PENGAJUAN:
        if p[2].lower() == nama.lower():
            raise ValueError("Kamu udah pernah ngajuin perangkat ini")

    id_peng = storage.tambah_pengajuan(username, nama, daya_int, durasi_float, tanggal)
    print("\n Pengajuan anda berhasil dikirim!")
    print(f"    ID        : {id_peng}")
    print(f"    Perangkat : {nama}")
    print(f"    Watt      : {daya_int} W")
    print(f"    Jam       : {storage.format_durasi(durasi_float)} jam")
    print(f"    Tanggal   : {tanggal}\n")
    print("    Tunggu di ACC admin ya")
    input("Tekan Enter untuk melanjutkan...")
