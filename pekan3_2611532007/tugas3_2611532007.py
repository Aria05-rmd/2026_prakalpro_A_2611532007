# Program kasir sederhana

nama_2007 = str(input("Masukkan nama pelanggan  : "))
status_2007 = str(input("Masukkan status pelanggan (member/nonmember) : ")).strip().lower()
total_2007 = int(input("Masukkan total belanja : "))
jumlah_2007 = int(input("Masukkan jumlah barang : "))
kode_2007 = str(input("Masukkan kode promo : "))

kode_promo_tersedia_2007 = ["HEMAT10","HEMAT20","GRATISONGKIR"]

print("\n===DATA TRANSAKSI===") 
print("Nama Pelanggan          : ", nama_2007)
print("Status Pelanggan        : ", status_2007)
print("Jumlah Barang           : ", jumlah_2007)
print("Kode Promo              : ", kode_2007)

print("\n===HASIL VALIDASI===")

v_belanja = total_2007 >= 200000
v_jumlah = jumlah_2007 >= 3
v_status = status_2007 == "member"
v_kode = kode_2007 in kode_promo_tersedia_2007
v_diskon = v_belanja
v_promo = v_jumlah

print("Belanja >= 200000       : ", v_belanja)
print("Jumlah Barang >= 3      : ", v_jumlah)
print("Status == Member        : ", v_status)
print("Kode Promo Tersedia     : ", v_kode)
print("Mendapatkan Diskon      : ", v_diskon or v_promo)
print("Mendapatkan Promo       : ", v_promo)

if kode_2007 == "HEMAT10":
  diskon_2007 = total_2007 * 0.10
elif kode_2007 == "HEMAT20":
  diskon_2007 = total_2007 * 0.20
else : diskon_2007 = 0

total_2007 -= diskon_2007

print("\n=== HASIL PERHITUNGAN ===")
print("Diskon                  : ",diskon_2007)
print("Total Pembayaran        : ", total_2007 )
print("Rata - rata Harga Barang: ", total_2007 / jumlah_2007)

print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses          : .....")
print("Member Access           :", v_status)
print("Promo Access            :", v_promo)
print("Free Shiping Access     : .....")

kode_transaksi_1021 = int(v_status) << 0 | int(v_belanja) << 1 | int(v_jumlah) << 2 | int(v_promo) << 3
kode_referensi_1021 = int(v_status) << 0 | int(v_belanja) << 1 | int(v_promo) << 3

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print(f"{format(int(v_status) << 0,"04b")} | {format(int(v_belanja) << 1,"04b")} | {format(int(v_jumlah) << 2,"04b")} | {format(int(v_promo) << 3,"04b")}")
print(f"Kode Biner   : {format(kode_transaksi_1021,"04b")}")
print(f"Kode Desimal : {kode_transaksi_1021}")

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{format(kode_transaksi_1021,"04b")} & {format(int(v_status) << 0,"04b")}")
print(f"Hasil Biner   : {format((kode_transaksi_1021) & int(v_status) << 0,"04b")}")
print(f"Hasil Desimal : {(kode_transaksi_1021) & int(v_status) << 0}")

print("Cek Promo")
print(f"{format(kode_transaksi_1021,"04b")} & {format(int(v_promo) << 3,"04b")}")
print(f"Hasil Biner   : {format((kode_transaksi_1021) & int(v_promo) << 3,"04b")}")
print(f"Hasil Desimal : {(kode_transaksi_1021) & int(v_promo) << 3}")

print("\n=== Perbandingan Status ===")
print(f"Kode Transaksi : {format(kode_transaksi_1021,"04b")}")
print(f"Kode Referensi : {format(kode_referensi_1021,"04b")}")
print(f"{format(kode_transaksi_1021,"04b")} ^ {format(kode_referensi_1021,"04b")}")
print(f"Hasil Biner   : {format((kode_transaksi_1021) ^ (kode_referensi_1021),"04b")}")
print(f"Hasil Desimal : {(kode_transaksi_1021) ^ (kode_referensi_1021)}")

print("\n=== Shift ===")
print(f"{format(kode_transaksi_1021,"04b")} << 1")
print(f"Hasil Biner   : {format((kode_transaksi_1021) << 1,"04b")}")
print(f"Hasil Desimal : {(kode_transaksi_1021) << 1}") 
print("=== SELESAI ===")