import storage

def hapus_data_admin():
    storage.bersihkan_layar()
    print("=== HAPUS DATA ===")
    for d in storage.DATA_LISTRIK:
        print(f"{d[0]}. {d[1]} - {d[4]}")
    print("")
    idx_input = input("ID yang mau dihapus (0 buat batal): ").strip()

    if idx_input == "0":
        print("Gajadi hapus")
        input("Tekan Enter untuk melanjutkan...")
        return
    try:
        idx = int(idx_input)
    except ValueError:
        raise ValueError("ID harus angka")

    posisi = storage.cari_index_listrik(idx)
    if posisi == -1:
        raise ValueError("Sayang banget ID mu gak ketemu")

    tanya = input(f"Yakin mau hapus {storage.DATA_LISTRIK[posisi][1]}? (y/n): ").lower()
    if tanya == "y":
        storage.hapus_data_listrik(posisi)
        print("[+] Data udah dihapus")
    else:
        print("Gajadi hapus")
    input("Tekan Enter untuk melanjutkan...")
