# Buat file dengan nama assignment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Python

angka1_2007 = int(input("Input angka-1: "))
angka2_2007 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_2007)
print("Nilai angka2 =", angka2_2007)

# Assignment biasa
hasil_2007 = angka1_2007
print("\nAssignment biasa(=)")
print("Hasil =",hasil_2007)

# Assignment penambahan
hasil_2007 = angka1_2007
hasil_2007 += angka2_2007
print("\nAssignment penambahan(+=)")
print("Hasil =", hasil_2007)

# Assignment pengurangan
hasil_2007 = angka1_2007
hasil_2007 -= angka2_2007
print("\nAssignment pengurangan(-=)")
print("Hasil =", hasil_2007)

# Assignment perkalian
hasil_2007 = angka1_2007
hasil_2007 *= angka2_2007
print("\nAssignment perkalian(*=)")
print("Hasil =", hasil_2007)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_2007 != 0:
    hasil_2007 = angka1_2007
    hasil_2007 /= angka2_2007
    print("\nAssignment pembagian(/=)")
    print("Hasil =", hasil_2007)

    hasil_2007 = angka1_2007
    hasil_2007 //= angka2_2007
    print("\nAssignment pembagian bulat(//=)")
    print("Hasil =", hasil_2007)
    
    hasil_2007 = angka1_2007
    hasil_2007 %= angka2_2007
    print("\nAssignment sisa bagi(%=)")
    print("Hasil =", hasil_2007)
else:
    print("\nAngka kedua tidak boleh bernilai 0.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil_2007= angka1_2007
hasil_2007 **= angka2_2007
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_2007)