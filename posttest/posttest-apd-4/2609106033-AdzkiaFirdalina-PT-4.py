# Program Kursus Bahasa Inggris dengan Login dan Input Data Siswa
USERNAME_TERDAFTAR = "kiki"
PASSWORD_TERDAFTAR = "033"

# Login user dengan maksimal 3 percobaan
login_berhasil = False
percobaan = 0

while percobaan < 3:
    print(f"\nPercobaan login ke-{percobaan + 1}")
    print("=== LOGIN KURSUS BAHASA INGGRIS ===")
    username_input = input("Masukkan username: ").strip()
    password_input = input("Masukkan password: ").strip()

    if username_input.lower() == USERNAME_TERDAFTAR and password_input == PASSWORD_TERDAFTAR:
        print("\nLogin berhasil!")
        login_berhasil = True
        break
    else:
        percobaan += 1
        print(f"\nLogin gagal! Username atau password salah.")
        print(f"Sisa percobaan: {3 - percobaan}")

if not login_berhasil:
    print("\nAnda telah mencapai batas percobaan login. Program dihentikan.")
else:
    # Input data siswa
    data_siswa = []

    while True:
        print("\n=== INPUT DATA SISWA ===")

        # Input nama siswa
        while True:
            nama_siswa = input("Masukkan nama siswa: ").strip()
            if nama_siswa == "":
                print("Nama siswa tidak boleh kosong. Silakan input ulang.")
            else:
                break

        # Input kelas
        kelas_siswa = input("Masukkan kelas siswa (A/B/C): ").strip().upper()

        # Input apakah siswa mengikuti ujian
        while True:
            ikut = input("Apakah siswa mengikuti ujian? (y/t): ").strip().lower()
            if ikut in ["y", "ya", "t", "tidak"]:
                break
            print("Masukkan y/ya atau t/tidak.")

        # Kalau tidak ikut ujian -> nilai 0
        if ikut in ["t", "tidak"]:
            ikut_ujian = False
            benar = 0
            salah = 0
            nilai = 0
            kategori = "Tidak ikut ujian"
        else:
            ikut_ujian = True

            # Input nilai siswa dengan validasi jumlah soal benar dan salah
            while True:
                try:
                    benar = int(input("Masukkan jumlah soal benar: "))
                    salah = int(input("Masukkan jumlah soal salah: "))

                    if benar < 0 or salah < 0:
                        print("Jumlah soal tidak boleh negatif.")
                    elif benar + salah != 20:
                        print("Total soal benar + salah harus 20.")
                    else:
                        break
                except ValueError:
                    print("Masukkan angka yang valid.")

            nilai = benar * 5

            # mengkategorikan nilai siswa
            if 80 <= nilai <= 100:
                kategori = "Sangat Baik"
            elif 60 <= nilai <= 79:
                kategori = "Baik"
            elif 40 <= nilai <= 59:
                kategori = "Cukup"
            else:
                kategori = "Perlu belajar lagi"

        # Simpan ke list
        data_siswa.append({
            "nama": nama_siswa,
            "kelas": kelas_siswa,
            "ikut_ujian": ikut_ujian,
            "nilai": nilai,
            "kategori": kategori
        })

        # apakah user ingin input data lagi
        while True:
            lagi = input("Masih ingin input data? (y/t): ").strip().lower()
            if lagi in ["y", "ya", "t", "tidak"]:
                break
            print("Masukkan y/ya atau t/tidak.")

        if lagi in ["t", "tidak"]:
            break

    # output hasil nilai siswa
    print("\n" + "=" * 80)
    print("HASIL NILAI SISWA KURSUS BAHASA INGGRIS")
    print("=" * 80)

    if len(data_siswa) == 0:
        print("Belum ada data siswa.")
    else:
        # Kumpulkan daftar kelas
        daftar_kelas = []
        for siswa in data_siswa:
            if siswa["kelas"] not in daftar_kelas:
                daftar_kelas.append(siswa["kelas"])
        daftar_kelas.sort()

        for kelas in daftar_kelas:
            print(f"\nKELAS: {kelas}")
            print("-" * 80)
            print(f"{'Nama Siswa':20} | {'Ikut Ujian':10} | {'Nilai':5} | {'Kategori':18}")
            print("-" * 80)

            for siswa in data_siswa:
                if siswa["kelas"] == kelas:
                    if siswa["ikut_ujian"]:
                        ikut_str = "Ya"
                    else:
                        ikut_str = "Tidak"

                    print(
                        f"{siswa['nama']:20} | "
                        f"{ikut_str:10} | "
                        f"{siswa['nilai']:5} | "
                        f"{siswa['kategori']:18}"
                    )

    # Simpan data ke file teks
    with open("data_siswa.txt", "w") as file:
        file.write("=== DATA NILAI SISWA KURSUS BAHASA INGGRIS ===\n")
        file.write(f"{'Nama Siswa':20} | {'Kelas':6} | {'Ikut Ujian':10} | {'Nilai':5} | {'Kategori':18}\n")
        file.write("=" * 80 + "\n")
        for siswa in data_siswa:
            if siswa["ikut_ujian"]:
                ikut_str = "Ya"
            else:
                ikut_str = "Tidak"
            file.write(
                f"{siswa['nama']:20} | "
                f"{siswa['kelas']:6} | "
                f"{ikut_str:10} | "
                f"{siswa['nilai']:5} | "
                f"{siswa['kategori']:18}\n"
            )
    print("\nData juga telah disimpan ke 'data_siswa.txt'")
