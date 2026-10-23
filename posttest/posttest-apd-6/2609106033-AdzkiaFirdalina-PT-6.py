import os
import datetime

# ============================================
# DATA USER (Dictionary)
# username : {password, role}
# ============================================
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "kiki":  {"password": "kiki123",  "role": "user"}
}

# ============================================
# DATA LISTRIK (Dictionary)
# id : {nama, daya, durasi, tanggal}
# ============================================
data_listrik = {
    1: {"nama": "Lampu",       "daya": 10,  "durasi": 5,  "tanggal": "12-10-2026"},
    2: {"nama": "Kipas Angin", "daya": 50,  "durasi": 8,  "tanggal": "12-10-2026"},
    3: {"nama": "Kulkas",      "daya": 100, "durasi": 24, "tanggal": "12-10-2026"}
}

# ============================================
# DATA PENGAJUAN (Dictionary)
# id : {user, nama, daya, durasi, tanggal}
# ============================================
pengajuan = {}

TARIF = 1444.7

# ============================================
# LOOP UTAMA (LOGIN / REGISTER)
# ============================================
while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 50)
    print("        WELCOME TO WATTWISE")
    print("   Monitor Ur Electricity Usage")
    print("=" * 50)
    username = input("Username : ").strip().lower()
    password = input("Password : ").strip().lower()

    # ---------- CEK USER ADA ATAU TIDAK ----------
    if username not in users:
        print("")
        print("Username " + username + " anda belum terdaftar.")
        jawab = input("Registrasi sekarang? (y/n): ")
        if jawab == "y" or jawab == "Y":
            nu = input("Username baru : ").strip().lower()
            np = input("Password baru : ").strip().lower()
            if nu == "":
                print("Username gak boleh kosong")
            elif np == "":
                print("Password gak boleh kosong")
            elif nu in users:
                print("Username udah dipake, cari yang lain")
            else:
                users[nu] = {"password": np, "role": "user"}
                print("Berhasil daftar! Silakan login pake username: " + nu)
            input("Tekan Enter untuk melanjutkan...")
        else:
            print("")
            print("Yaudah keluar dulu ya. Terima kasih!")
            break
        continue

    # ---------- CEK PASSWORD ----------
    if users[username]["password"] != password:
        print("")
        print("Password salah!")
        input("Tekan Enter untuk melanjutkan...")
        continue

    role = users[username]["role"]
    ketemu = True
    print("")
    print("Login sebagai " + role.upper() + ". Halo, " + username + "!")
    input("Tekan Enter untuk melanjutkan...")

    # ============================================
    # LOOP MENU SETELAH LOGIN
    # ============================================
    while ketemu == True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 50)
        print("   MENU " + role.upper() + " - " + username)
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
        pilih = input("Pilih: ")

        # ============================================
        # 1. VIEW DATA BILING (admin & user)
        # ============================================
        if pilih == "1":
            os.system("cls" if os.name == "nt" else "clear")
            print("=" * 70)
            print("            DAFTAR PENGGUNAAN LISTRIK")
            print("=" * 70)
            if len(data_listrik) == 0:
                print("Belum ada data")
            else:
                print("ID  Perangkat        Daya   Jam   Tanggal        kWh")
                print("-" * 70)
                total = 0
                for id_d, d in data_listrik.items():
                    kwh = d["daya"] * d["durasi"] / 1000
                    total = total + kwh
                    print(str(id_d) + "   " + d["nama"] + "   " + str(d["daya"]) + "W   " + str(d["durasi"]) + "j   " + d["tanggal"] + "   " + str(round(kwh, 3)))
                print("-" * 70)
                print("TOTAL : " + str(round(total, 3)) + " kWh  |  Rp " + str(round(total * TARIF, 2)))
            input("")
            input("Tekan Enter Untuk Melanjutkan...")

        # ============================================
        # 2. TAMBAH DATA BILING (admin)
        # ============================================
        elif pilih == "2" and role == "admin":
            os.system("cls" if os.name == "nt" else "clear")
            print("=== TAMBAH DATA ===")
            print("Ketik 0 di nama perangkat buat batal")
            print("")
            nama = input("Nama perangkat      : ").strip()
            if nama == "0":
                print("Gajadi nambah data")
            else:
                daya = input("Daya (Watt)         : ").strip()
                durasi = input("Durasi (jam)        : ").strip()
                tanggal = input("Tanggal (dd-mm-yyyy): ").strip()
                cek_durasi = durasi.replace(".", "", 1)
                tgl = tanggal.split("-")
                salah = False
                if nama == "":
                    print("Namanya jangan dikosongin")
                    salah = True
                elif daya.isdigit() == False:
                    print("Daya harus angka")
                    salah = True
                elif int(daya) <= 0:
                    print("Daya harus lebih dari 0")
                    salah = True
                elif cek_durasi.isdigit() == False:
                    print("Durasi harus angka")
                    salah = True
                elif float(durasi) <= 0:
                    print("Durasi harus lebih dari 0")
                    salah = True
                elif float(durasi) > 24:
                    print("Durasi sehari gak mungkin lebih dari 24 jam")
                    salah = True
                elif len(tgl) != 3:
                    print("Format tanggal salah, harusnya dd-mm-yyyy")
                    salah = True
                if salah == False:
                    for t in tgl:
                        if t.isdigit() == False:
                            print("Tanggal harus angka semua")
                            salah = True
                if salah == False:
                    dd = int(tgl[0])
                    mm = int(tgl[1])
                    yy = int(tgl[2])
                    if dd < 1 or dd > 31 or mm < 1 or mm > 12 or yy < 2000:
                        print("Tanggal gak valid")
                        salah = True
                if salah == False:
                    for id_d, d in data_listrik.items():
                        if d["nama"].lower() == nama.lower() and d["tanggal"] == tanggal:
                            print("Data ini udah ada")
                            salah = True
                if salah == False:
                    if len(data_listrik) == 0:
                        id_baru = 1
                    else:
                        id_baru = max(data_listrik.keys()) + 1
                    data_listrik[id_baru] = {"nama": nama, "daya": int(daya), "durasi": float(durasi), "tanggal": tanggal}
                    print("[+] Data berhasil ditambah, ID nya " + str(id_baru))
            input("Tekan Enter untuk melanjutkan...")

        # ============================================
        # 3. UBAH DATA BILING (admin)
        # ============================================
        elif pilih == "3" and role == "admin":
            os.system("cls" if os.name == "nt" else "clear")
            print("=== UBAH DATA ===")
            for id_d, d in data_listrik.items():
                print(str(id_d) + ". " + d["nama"] + " - " + str(d["daya"]) + "W - " + str(d["durasi"]) + "j - " + d["tanggal"])
            print("")
            idx = input("ID yang mau diubah (0 buat batal): ").strip()
            if idx == "0":
                print("Gajadi ubah")
            elif idx.isdigit() == False:
                print("ID harus angka")
            else:
                idx = int(idx)
                if idx not in data_listrik:
                    print("ID gak ketemu")
                else:
                    nama = input("Nama baru    : ").strip()
                    daya = input("Daya baru    : ").strip()
                    durasi = input("Durasi baru  : ").strip()
                    tanggal = input("Tanggal baru : ").strip()
                    cek_durasi = durasi.replace(".", "", 1)
                    tgl = tanggal.split("-")
                    salah = False
                    if nama == "":
                        print("Nama jangan kosong")
                        salah = True
                    elif daya.isdigit() == False:
                        print("Daya harus angka")
                        salah = True
                    elif int(daya) <= 0:
                        print("Daya harus lebih dari 0")
                        salah = True
                    elif cek_durasi.isdigit() == False:
                        print("Durasi harus angka")
                        salah = True
                    elif float(durasi) <= 0:
                        print("Durasi harus lebih dari 0")
                        salah = True
                    elif float(durasi) > 24:
                        print("Durasi sehari gak mungkin lebih dari 24 jam")
                        salah = True
                    elif len(tgl) != 3:
                        print("Format tanggal salah, harusnya dd-mm-yyyy")
                        salah = True
                    if salah == False:
                        for t in tgl:
                            if t.isdigit() == False:
                                print("Tanggal harus angka semua")
                                salah = True
                    if salah == False:
                        dd = int(tgl[0])
                        mm = int(tgl[1])
                        yy = int(tgl[2])
                        if dd < 1 or dd > 31 or mm < 1 or mm > 12 or yy < 2000:
                            print("Tanggal gak valid")
                            salah = True
                    if salah == False:
                        data_listrik[idx]["nama"] = nama
                        data_listrik[idx]["daya"] = int(daya)
                        data_listrik[idx]["durasi"] = float(durasi)
                        data_listrik[idx]["tanggal"] = tanggal
                        print("[+] Data udah diubah")
            input("Tekan Enter untuk melanjutkan...")

        # ============================================
        # 4. HAPUS DATA BILING (admin)
        # ============================================
        elif pilih == "4" and role == "admin":
            os.system("cls" if os.name == "nt" else "clear")
            print("=== HAPUS DATA ===")
            for id_d, d in data_listrik.items():
                print(str(id_d) + ". " + d["nama"] + " - " + d["tanggal"])
            print("")
            idx = input("ID yang mau dihapus (0 buat batal): ").strip()
            if idx == "0":
                print("Gajadi hapus")
            elif idx.isdigit() == False:
                print("ID harus angka")
            else:
                idx = int(idx)
                if idx not in data_listrik:
                    print("Sayang banget ID mu gak ketemu")
                else:
                    tanya = input("Yakin mau hapus " + data_listrik[idx]["nama"] + "? (y/n): ").lower()
                    if tanya == "y":
                        del data_listrik[idx]
                        print("[+] Data udah dihapus")
                    else:
                        print("Gajadi hapus")
            input("Tekan Enter untuk melanjutkan...")

        # ============================================
        # 5. LIHAT INFORMASI USER (admin)
        # ============================================
        elif pilih == "5" and role == "admin":
            os.system("cls" if os.name == "nt" else "clear")
            print("=== DAFTAR USER ===")
            no = 1
            for u in users:
                print(str(no) + ". " + u + " - " + users[u]["role"])
                no = no + 1
            input("")
            input("Tekan Enter untuk melanjutkan...")

        # ============================================
        # 6. TOTAL TAGIHAN (admin)
        # ============================================
        elif pilih == "6" and role == "admin":
            os.system("cls" if os.name == "nt" else "clear")
            print("=== TOTAL PENGGUNAAN ===")
            total = 0
            for id_d, d in data_listrik.items():
                kwh = d["daya"] * d["durasi"] / 1000
                total = total + kwh
                print("- " + d["nama"] + " : " + str(round(kwh, 3)) + " kWh  (Rp " + str(round(kwh * TARIF, 2)) + ")")
            print("-" * 45)
            print("TOTAL : " + str(round(total, 3)) + " kWh  |  Rp " + str(round(total * TARIF, 2)))
            input("")
            input("Tekan Enter untuk melanjutkan...")

        # ============================================
        # 7. LIHAT PENGAJUAN USER (admin)
        # ============================================
        elif pilih == "7" and role == "admin":
            os.system("cls" if os.name == "nt" else "clear")
            print("=== PENGAJUAN DARI USER ===")
            if len(pengajuan) == 0:
                print("Belum ada pengajuan nih")
            else:
                print("ID  User        Perangkat        Daya   Jam   Tanggal")
                print("-" * 65)
                for id_p, p in pengajuan.items():
                    print(str(id_p) + "   " + p["user"] + "   " + p["nama"] + "   " + str(p["daya"]) + "W   " + str(p["durasi"]) + "j   " + p["tanggal"])
                print("-" * 65)
                print("")
                id_pil = input("Masukkan ID pengajuan yang mau diproses (0 buat batal): ").strip()
                if id_pil == "0":
                    print("Gajadi proses")
                elif id_pil.isdigit() == False:
                    print("ID harus angka")
                else:
                    id_pil = int(id_pil)
                    if id_pil not in pengajuan:
                        print("ID pengajuan gak ketemu")
                    else:
                        print("")
                        print("Pengajuan dari : " + pengajuan[id_pil]["user"])
                        print("Perangkat      : " + pengajuan[id_pil]["nama"])
                        print("Daya           : " + str(pengajuan[id_pil]["daya"]) + " W")
                        print("Durasi         : " + str(pengajuan[id_pil]["durasi"]) + " jam")
                        print("Tanggal        : " + pengajuan[id_pil]["tanggal"])
                        print("")
                        aksi = input("Mau di-ACC atau ditolak? (acc/tolak): ").lower()
                        if aksi == "acc":
                            dobel = False
                            for id_d, d in data_listrik.items():
                                if d["nama"].lower() == pengajuan[id_pil]["nama"].lower() and d["tanggal"] == pengajuan[id_pil]["tanggal"]:
                                    dobel = True
                            if dobel == True:
                                print("Perangkat ini udah ada di data biling")
                            else:
                                if len(data_listrik) == 0:
                                    id_baru = 1
                                else:
                                    id_baru = max(data_listrik.keys()) + 1
                                data_listrik[id_baru] = {
                                    "nama":     pengajuan[id_pil]["nama"],
                                    "daya":     pengajuan[id_pil]["daya"],
                                    "durasi":   pengajuan[id_pil]["durasi"],
                                    "tanggal":  pengajuan[id_pil]["tanggal"]
                                }
                                del pengajuan[id_pil]
                                print("Pengajuan di-ACC, data udah masuk ke biling")
                        elif aksi == "tolak":
                            del pengajuan[id_pil]
                            print("Pengajuan ditolak")
                        else:
                            print("Pilihan gak ada, coba lagi")
            input("")
            input("Tekan Enter Untuk Melanjutkan...")

        # ============================================
        # 2. TOTAL KONSUMSI SAYA (user)
        # ============================================
        elif pilih == "2" and role == "user":
            os.system("cls" if os.name == "nt" else "clear")
            print("=== TOTAL PENGGUNAAN ANDA ===")
            total = 0
            for id_d, d in data_listrik.items():
                total = total + d["daya"] * d["durasi"] / 1000
            print("Harian  : " + str(round(total, 3)) + " kWh")
            print("Biaya   : Rp " + str(round(total * TARIF, 2)))
            print("Bulanan : Rp " + str(round(total * TARIF * 30, 2)))
            input("")
            input("Tekan Enter...")

        # ============================================
        # 3. AJUKAN PENAMBAHAN PERANGKAT (user)
        # ============================================
        elif pilih == "3" and role == "user":
            os.system("cls" if os.name == "nt" else "clear")
            print("=== AJUKAN PENAMBAHAN PERANGKAT ===")
            print("[i] Isi datanya, admin bakal tinjau dulu")
            print("")
            nama = input("Mau nambah perangkat apa? ").strip()
            daya = input("Berapa watt? ").strip()
            durasi = input("Berapa jam pemakaian per hari? ").strip()
            hari_ini = datetime.date.today()
            tanggal = str(hari_ini.day) + "-" + str(hari_ini.month) + "-" + str(hari_ini.year)
            cek_durasi = durasi.replace(".", "", 1)
            salah = False
            if nama == "":
                print("Nama perangkatnya jangan kosong")
                salah = True
            elif daya.isdigit() == False:
                print("Watt harus angka")
                salah = True
            elif int(daya) <= 0:
                print("Watt harus lebih dari 0")
                salah = True
            elif cek_durasi.isdigit() == False:
                print("Jam harus angka")
                salah = True
            elif float(durasi) <= 0:
                print("Jam harus lebih dari 0")
                salah = True
            elif float(durasi) > 24:
                print("Sehari gak mungkin lebih dari 24 jam")
                salah = True
            if salah == False:
                for id_d, d in data_listrik.items():
                    if d["nama"].lower() == nama.lower():
                        print("Perangkat ini udah ada di data biling")
                        salah = True
            if salah == False:
                for id_p, p in pengajuan.items():
                    if p["nama"].lower() == nama.lower():
                        print("Kamu udah pernah ngajuin perangkat ini")
                        salah = True
            if salah == False:
                if len(pengajuan) == 0:
                    id_peng = 1
                else:
                    id_peng = max(pengajuan.keys()) + 1
                pengajuan[id_peng] = {
                    "user":    username,
                    "nama":    nama,
                    "daya":    int(daya),
                    "durasi":  float(durasi),
                    "tanggal": tanggal
                }
                print("")
                print(" Pengajuan anda berhasil dikirim!")
                print("    Perangkat : " + nama)
                print("    Watt      : " + str(daya) + " W")
                print("    Jam       : " + str(durasi) + " jam")
                print("    Tanggal   : " + tanggal)
                print("")
                print("    Tunggu di ACC admin ya")
            input("")
            input("Tekan Enter Untuk Melanjutkan...")

        # ============================================
        # 0. LOGOUT
        # ============================================
        elif pilih == "0":
            ketemu = False
            print("")
            print("Yah, Logout dulu ya")
            input("Tekan Enter Untuk Melanjutkan...")

        else:
            print("Yhaaaa Pilihannya gak ada, silahkan coba lagi")
            input("Tekan Enter Untuk Melanjutkan...")
