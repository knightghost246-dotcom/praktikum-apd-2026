# Program simulasi transaksi pengisian BBM di SPBU
NAMA_PANGGILAN = "Kiki".lower()
NIM = "33" [-2:]

print("=== LOGIN SPBU ===")
nama_input = input("Masukkan nama panggilan: ")
nim_input = input("Masukkan 2 digit terakhir NIM: ")

if nama_input == NAMA_PANGGILAN and NIM == NIM:
    print("\nLogin berhasil!")

    print("\n=== MENU BBM ===")
    print("1. Pertalite       : Rp 10.000/liter")
    print("2. Pertamax        : Rp 12.500/liter")
    print("3. Pertamax Turbo  : Rp 15.000/liter")

    pilihan_jenis_bbm = input("Pilihlah anda ingin mengisi BBM dengan jenis apa (1-3): ")

    if pilihan_jenis_bbm == "1":
        jenis_bbm = "Pertalite"
        harga_per_liter = 10000
    elif pilihan_jenis_bbm == "2":
        jenis_bbm = "Pertamax"
        harga_per_liter = 12500
    elif pilihan_jenis_bbm == "3":
        jenis_bbm = "Pertamax Turbo"
        harga_per_liter = 15000
    else:
        jenis_bbm = "Tidak valid"
        harga_per_liter = 0

    if harga_per_liter > 0:
        liter = float(input("Masukkan berapa liter yang ingin anda beli: ").replace(",", "."))

        total_harga = harga_per_liter * liter

        # Diskon berdasarkan jumlah liter
        if liter >= 10:
            persen_diskon = 0.10
        elif liter >= 5:
            persen_diskon = 0.05
        else:
            persen_diskon = 0.00

        diskon_pembelian = persen_diskon * total_harga

        # Status member
        member = input("Apakah pembeli member? (y/n): ").lower()

        if member == "y" or member == "ya":
            status_member = "Member"
            persen_member = 0.02
        else:
            status_member = "Non-member"
            persen_member = 0.00

        diskon_member = persen_member * total_harga

        total_bayar = total_harga - diskon_pembelian - diskon_member

        print("\n" + "=" * 55)
        print("STRUK TRANSAKSI PENGISIAN BBM".center(55))
        print("=" * 55)
        print(f"{'Nama Pembeli':<22}: {nama_input}")
        print(f"{'NIM':<22}: {NIM}")
        print(f"{'Jenis BBM':<22}: {jenis_bbm}")
        print(f"{'Harga/Liter':<22}: Rp {harga_per_liter:,.0f}".replace(",", "."))
        print(f"{'Jumlah Liter':<22}: {liter:.2f} Liter")
        print(f"{'Total Harga':<22}: Rp {total_harga:,.0f}".replace(",", "."))
        print(f"{'Diskon Pembelian':<22}: Rp {diskon_pembelian:,.0f} ({persen_diskon * 100:.0f}%)".replace(",", "."))
        print(f"{'Status Member':<22}: {status_member}")
        print(f"{'Diskon Member':<22}: Rp {diskon_member:,.0f} ({persen_member * 100:.0f}%)".replace(",", "."))
        print(f"{'Total Bayar':<22}: Rp {total_bayar:,.0f}".replace(",", "."))
        print("=" * 55)

    else:
        print("Pilihan BBM tidak valid. Transaksi dibatalkan.")

else:
    print("Login gagal! Program berhenti.")
