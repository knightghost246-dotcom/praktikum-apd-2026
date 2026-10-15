import os
import datetime

users = [
    ["admin","admin123","admin"],
    ["kiki","kiki123","user"]
]
data_listrik = [
    [1,"Lampu",10,5,"12-10-2026"],
    [2,"Kipas Angin",50,8,"12-10-2026"],
    [3,"Kulkas",100,24,"12-10-2026"]
]
pengajuan = []
TARIF = 1444.7

while True:
    os.system("cls" if os.name == "nt" else "clear")
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
        print("Username " + username + " anda belum terdaftar.")
        jawab = input("Registrasi sekarang? (y/n): ")
        if jawab == "y" or jawab == "Y":
            nu = input("Username baru : ").strip().lower()
            np = input("Password baru : ").strip().lower()
            udah_pake = False
            for x in users:
                if x[0] == nu:
                    udah_pake = True
            if nu == "":
                print("Username gak boleh kosong")
            elif np == "":
                print("Password gak boleh kosong")
            elif udah_pake == True:
                print("Username udah dipake, cari yang lain")
            else:
                users.append([nu, np, "user"])
                print("Berhasil daftar! Silakan login pake username: " + nu)
            input("Tekan Enter untuk melanjutkan...")
        else:
            print("")
            print("Yaudah keluar dulu ya. Terima kasih!")
            break
        continue
    ketemu = False
    role = ""
    for x in users:
        if x[0] == username and x[1] == password:
            ketemu = True
            role = x[2]
    if ketemu == False:
        print("")
        print("Password salah!")
        input("Tekan Enter untuk melanjutkan...")
        continue
    print("")
    print("Login sebagai " + role.upper() + ". Halo, " + username + "!")
    input("Tekan Enter untuk melanjutkan...")

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
                for d in data_listrik:
                    kwh = d[2] * d[3] / 1000
                    total = total + kwh
                    print(str(d[0]) + "   " + d[1] + "   " + str(d[2]) + "W   " + str(d[3]) + "j   " + d[4] + "   " + str(round(kwh, 3)))
                print("-" * 70)
                print("TOTAL : " + str(round(total, 3)) + " kWh  |  Rp " + str(round(total * TARIF, 2)))
            input("")
            input("Tekan Enter Untuk Melanjutkan...")
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
                cek_durasi = durasi.replace(".","",1)
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
                    for d in data_listrik:
                        if d[1].lower() == nama.lower() and d[4] == tanggal:
                            print("Data ini udah ada")
                            salah = True
                if salah == False:
                    if len(data_listrik) == 0:
                        id_baru = 1
                    else:
                        id_baru = data_listrik[-1][0] + 1
                    data_listrik.append([id_baru, nama, int(daya), float(durasi), tanggal])
                    print("[+] Data berhasil ditambah, ID nya " + str(id_baru))
            input("Tekan Enter untuk melanjutkan...")
        elif pilih == "3" and role == "admin":
            os.system("cls" if os.name == "nt" else "clear")
            print("=== UBAH DATA ===")
            for d in data_listrik:
                print(str(d[0]) + ". " + d[1] + " - " + str(d[2]) + "W - " + str(d[3]) + "j - " + d[4])
            print("")
            idx = input("ID yang mau diubah (0 buat batal): ").strip()
            if idx == "0":
                print("Gajadi ubah")
            elif idx.isdigit() == False:
                print("ID harus angka")
            else:
                idx = int(idx)
                posisi = -1
                for i in range(len(data_listrik)):
                    if data_listrik[i][0] == idx:
                        posisi = i
                if posisi == -1:
                    print("ID gak ketemu")
                else:
                    nama = input("Nama baru    : ").strip()
                    daya = input("Daya baru    : ").strip()
                    durasi = input("Durasi baru  : ").strip()
                    tanggal = input("Tanggal baru : ").strip()
                    cek_durasi = durasi.replace(".","",1)
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
                        data_listrik[posisi][1] = nama
                        data_listrik[posisi][2] = int(daya)
                        data_listrik[posisi][3] = float(durasi)
                        data_listrik[posisi][4] = tanggal
                        print("[+] Data udah diubah")
            input("Tekan Enter untuk melanjutkan...")
        elif pilih == "4" and role == "admin":
            os.system("cls" if os.name == "nt" else "clear")
            print("=== HAPUS DATA ===")
            for d in data_listrik:
                print(str(d[0]) + ". " + d[1] + " - " + d[4])
            print("")
            idx = input("ID yang mau dihapus (0 buat batal): ").strip()
            if idx == "0":
                print("Gajadi hapus")
            elif idx.isdigit() == False:
                print("ID harus angka")
            else:
                idx = int(idx)
                posisi = -1
                for i in range(len(data_listrik)):
                    if data_listrik[i][0] == idx:
                        posisi = i
                if posisi == -1:
                    print("Sayang banget ID mu gak ketemu")
                else:
                    tanya = input("Yakin mau hapus " + data_listrik[posisi][1] + "? (y/n): ").lower()
                    if tanya == "y":
                        data_listrik.pop(posisi)
                        print("[+] Data udah dihapus")
                    else:
                        print("Gajadi hapus")
            input("Tekan Enter untuk melanjutkan...")
        elif pilih == "5" and role == "admin":
            os.system("cls" if os.name == "nt" else "clear")
            print("=== DAFTAR USER ===")
            no = 1
            for x in users:
                print(str(no) + ". " + x[0] + " - " + x[2])
                no = no + 1
            input("")
            input("Tekan Enter untuk melanjutkan...")
        elif pilih == "6" and role == "admin":
            os.system("cls" if os.name == "nt" else "clear")
            print("=== TOTAL PENGGUNAAN ===")
            total = 0
            for d in data_listrik:
                kwh = d[2] * d[3] / 1000
                total = total + kwh
                print("- " + d[1] + " : " + str(round(kwh, 3)) + " kWh  (Rp " + str(round(kwh * TARIF, 2)) + ")")
            print("-" * 45)
            print("TOTAL : " + str(round(total, 3)) + " kWh  |  Rp " + str(round(total * TARIF, 2)))
            input("")
            input("Tekan Enter untuk melanjutkan...")
        elif pilih == "7" and role == "admin":
            os.system("cls" if os.name == "nt" else "clear")
            print("=== PENGAJUAN DARI USER ===")
            if len(pengajuan) == 0:
                print("Belum ada pengajuan nih")
            else:
                print("ID  User        Perangkat        Daya   Jam   Tanggal")
                print("-" * 65)
                for p in pengajuan:
                    print(str(p[0]) + "   " + p[1] + "   " + p[2] + "   " + str(p[3]) + "W   " + str(p[4]) + "j   " + p[5])
                print("-" * 65)
                print("")
                id_pil = input("Masukkan ID pengajuan yang mau diproses (0 buat batal): ").strip()
                if id_pil == "0":
                    print("Gajadi proses")
                elif id_pil.isdigit() == False:
                    print("ID harus angka")
                else:
                    id_pil = int(id_pil)
                    posisi = -1
                    for i in range(len(pengajuan)):
                        if pengajuan[i][0] == id_pil:
                            posisi = i
                    if posisi == -1:
                        print("ID pengajuan gak ketemu")
                    else:
                        print("")
                        print("Pengajuan dari : " + pengajuan[posisi][1])
                        print("Perangkat      : " + pengajuan[posisi][2])
                        print("Daya           : " + str(pengajuan[posisi][3]) + " W")
                        print("Durasi         : " + str(pengajuan[posisi][4]) + " jam")
                        print("Tanggal        : " + pengajuan[posisi][5])
                        print("")
                        aksi = input("Mau di-ACC atau ditolak? (acc/tolak): ").lower()
                        if aksi == "acc":
                            dobel = False
                            for d in data_listrik:
                                if d[1].lower() == pengajuan[posisi][2].lower() and d[4] == pengajuan[posisi][5]:
                                    dobel = True
                            if dobel == True:
                                print("Perangkat ini udah ada di data biling")
                            else:
                                if len(data_listrik) == 0:
                                    id_baru = 1
                                else:
                                    id_baru = data_listrik[-1][0] + 1
                                data_listrik.append([id_baru, pengajuan[posisi][2], pengajuan[posisi][3], pengajuan[posisi][4], pengajuan[posisi][5]])
                                pengajuan.pop(posisi)
                                print("Pengajuan di-ACC, data udah masuk ke biling")
                        elif aksi == "tolak":
                            pengajuan.pop(posisi)
                            print("Pengajuan ditolak")
                        else:
                            print("Pilihan gak ada, coba lagi")
            input("")
            input("Tekan Enter Untuk Melanjutkan...")
        elif pilih == "2" and role == "user":
            os.system("cls" if os.name == "nt" else "clear")
            print("=== TOTAL PENGGUNAAN ANDA ===")
            total = 0
            for d in data_listrik:
                total = total + d[2] * d[3] / 1000
            print("Harian  : " + str(round(total, 3)) + " kWh")
            print("Biaya   : Rp " + str(round(total * TARIF, 2)))
            print("Bulanan : Rp " + str(round(total * TARIF * 30, 2)))
            input("")
            input("Tekan Enter...")
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
            cek_durasi = durasi.replace(".","",1)
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
                for d in data_listrik:
                    if d[1].lower() == nama.lower():
                        print("Perangkat ini udah ada di data biling")
                        salah = True
            if salah == False:
                for p in pengajuan:
                    if p[2].lower() == nama.lower():
                        print("Kamu udah pernah ngajuin perangkat ini")
                        salah = True
            if salah == False:
                if len(pengajuan) == 0:
                    id_peng = 1
                else:
                    id_peng = pengajuan[-1][0] + 1
                pengajuan.append([id_peng, username, nama, int(daya), float(durasi), tanggal])
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
        elif pilih == "0":
            ketemu = False
            print("")
            print("Yah, Logout dulu ya")
            input("Tekan Enter Untuk Melanjutkan...")
        else:
            print("Yhaaaa Pilihannya gak ada, silahkan coba lagi")
            input("Tekan Enter Untuk Melanjutkan...")
