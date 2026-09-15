# Buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_2007 = int(input("Input angka-1: "))
angka2_2007 = int(input("Input angka-2: "))
                        
# Lebih besar dari
hasil_2007= angka1_2007 > angka2_2007
print("\nOperator lebih besar dari")
print("angka1_2007 > angka2_2007 =", hasil_2007)
      
# Lebih kecil dari
hasil_2007 = angka1_2007 < angka2_2007 
print("\nOperator lebih kecil dari")
print("angka1_2007 < angka2_2007 =", hasil_2007)

# Lebih besar dari atau sama dengan
hasil_2007 = angka1_2007 >= angka2_2007
print("\nOperator lebih besar dari atau sama dengan")
print("angka1_2007 >= angka2_2007 =", hasil_2007)

# Lebih kecil dari atau sama dengan
hasil_2007 = angka1_2007 <= angka2_2007
print("\nOperator lebih kecil dari atau sama dengan")
print("angka1_2007 <= angka2_2007 =", hasil_2007)

# Sama dengan
hasil_2007 = angka1_2007 == angka2_2007
print("\nOperator sama dengan")
print("angka1_2007 == angka2_2007 =", hasil_2007)

# Tidak sama dengan
hasil_2007 = angka1_2007 != angka2_2007
print("\nOperator tidak sama dengan")
print("angka1_2007 != angka2_2007 =", hasil_2007)

# Tambahan: perbandingan berantai dalam Python
hasil_2007 = 0 < angka1_2007 < 100
print("\nPerbandingan berantai")
print("0 < angka1_2007 < 100 =", hasil_2007)

hasil_2007 = 0 < angka2_2007 < 100
print("0 < angka2_2007 < 100 =", hasil_2007 )