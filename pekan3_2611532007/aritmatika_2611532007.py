# Buat file dengan nama aritmatika_2611532007.py
# Buat program untuk operator arimatika dalam python
# Nama variable ditambah 4 digit nim terakhir contoh: angka1_2007
# Program ini menggunakan fungsi input()
# Nilai yang dimasukan akan di konversikan menjadi tipe data integer

angka1_2007=int(input("input angka-1:"))
angka2_2007=int(input("input angka-2:"))

# Penjumlahan 
hasil_2007 = angka1_2007 + angka2_2007
print("nOperator Penjumlahan")
print("Hasil =", hasil_2007)

# Pengurangan
hasil_2007 = angka1_2007 - angka2_2007
print("nOperator Pengurangan")
print("Hasil =", hasil_2007)

# Perkalian
hasil_2007 = angka1_2007 * angka2_2007
print("\nOperator Perkalian")
print("Hasil =", hasil_2007)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_2007 != 0:
    hasil_2007 = angka1_2007 / angka2_2007
    print("\nOperator Pembagian")
    print("Hasil =", hasil_2007)

    hasil_2007 = angka1_2007 // angka2_2007
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_2007)
    
    hasil_2007 = angka1_2007 % angka2_2007
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_2007)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_2007 = angka1_2007 ** angka2_2007
print("\nOperator Pangkat")
print("Hasil =", hasil_2007)