# Sistem loket terpadu & audit tranksaksi ekspedisi wahana
print("|=======================================|")
print("|== SISTEM LOKET ALPRO ADVENTURE PARK ==|")
print("|=======================================|")

nama_pengunjung_2007 = str(input("Nama Pengunjung: "))
umur_2007 = int(input("Umur Pengunjung: "))
kartu_sim_2007 = str(input("Memiliki Kartu Identitas/SIM C (y/t): "))[0].strip().lower()
jumlah_tiket_2007 = int(input("Jumlah ticket: "))
is_member_2007 = str(input("Apakah Member? (y/t): "))[0].strip().lower()
kode_promo_2007 = str(input("Kode Promo: "))
kode_valid_2007 = ["1234","1324","5544"]

print("Nama Pengunjung: ", nama_pengunjung_2007)
print("Umur Pengunjung: ", umur_2007)
print("Apakah Sudah Punya SIM C (y/t): ", kartu_sim_2007)
print("Kode Promo: ", kode_promo_2007)

if jumlah_tiket_2007 <= 0:
    print("Peringatan Kuota Ticket Tidak Valid")

# Pilihan paket Wahana

print("Pilihan Paket Wahana (1-5): ")
print("1. Safari Rimba         (Rp 50,000)")
print("2. Arung Jeram          (Rp 75,000)")
print("3. Motor ATV Ekstrim    (Rp 120,000)")
print("4. Roller Coaster Kilat (Rp 100,000)")
print("5. All-Access VIP       (Rp 220,000)")

paket_wahana_2007 = int(input("Masukkan Nomor Paket Wahana: "))
harga_satuan_2007 = 0
match paket_wahana_2007:
    case 1: 
        harga_satuan_2007 = 50000
        print("Wahana Safari Rimba |", harga_satuan_2007)
    case 2: 
        harga_satuan_2007 = 75000
        print("Wahana Arung Jeram |", harga_satuan_2007)
    case 3:
        harga_satuan_2007 = 120000
        print("Wahana Motor ATV Ekstrim |", harga_satuan_2007)
    case 4:
        harga_satuan_2007 = 100000
        print("Wahana Roller Coaster Kilat |", harga_satuan_2007)
    case 5:
        harga_satuan_2007 = 220000
        print("Wahana All Access VIP |", harga_satuan_2007)
    case _:
        print("Paket Wahana Tidak Valid").exit()

# Validasi Izin Kendali

print("\n~~~~ Kelayakan Pengendara Wahana ~~~~")

if paket_wahana_2007 == 3 :
    if umur_2007 >= 17 and kartu_sim_2007 == 'y':
        print("Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
    elif umur_2007  >= 17 and kartu_sim_2007 != 'y':
        print("Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
    elif umur_2007 < 17 and kartu_sim_2007 == 'y':
        print( "Identitas tidak valid: Belum cukup umur memiliki SIM.")
    else :
        print("Anda belum cukup umur dan tidak boleh bawa motor ATV.")
else:
    if umur_2007 >= 10:
        print("Anda Mencukupi Umur")
    else:
        print("Anda Tidak Mencukupi Umur")

# Akumulasi Diskon 
harga_subtotal_2007 = harga_satuan_2007 * jumlah_tiket_2007
total_diskon_2007 = 0

if harga_subtotal_2007 >= 200000:
    total_diskon_2007 += 10
if is_member_2007 in ['y',"ya"]:
    total_diskon_2007 += 5
if kode_promo_2007 in kode_valid_2007:
    total_diskon_2007 += 15
if jumlah_tiket_2007 >= 5:
  total_diskon_2007 += 5

# Alur Eksekusi

print("\n~~~~ Rincian Belanja ~~~~")

nominal_diskon_2007 = harga_subtotal_2007 * total_diskon_2007 / 100
total_bayar = harga_subtotal_2007 - nominal_diskon_2007

print(f"Subtotal Belanja: Rp {harga_subtotal_2007:,.0f}")
print(f"Total Diskon: {total_diskon_2007}% (Rp {nominal_diskon_2007:,.0f})")
print(f"Total Bayar: Rp {total_bayar:,.0f}")

if total_bayar > 300000:
    print("Catatan Layanan : Selamat Anda berhak mendapatkan Souvenir Gratis")
else:
    print("Catatan Layanan : Terimakasih Telah Berkunjung")

print("Program Selesai")

