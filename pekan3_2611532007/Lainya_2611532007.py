# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("==================================")
print("1. OPERATOR KEANGGOTAAN")
print("==================================")

# Input beberapa data yang dipisahkan dengan koma
input_data = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data =[int(angka.strip())for angka in input_data.split(",")]

nilai_dicari = int(input("Masukkan angka yang ingin dicari:"))

# Operator in
hasil_2007= nilai_dicari in data
print("\noperator keanggotaan IN")
print(nilai_dicari,"in", data,"=", hasil_2007)

# Operator not in
hasil_2007 = nilai_dicari not in data
print("\noperator keanggotaan NOT IN")
print(nilai_dicari,"not in", data,"=", hasil_2007)

print("\n==================================")
print("2. OPERATOR IDENTITAS")
print("==================================")

# objek1 menggunakan list dari input pengguna
objek1_2007 = data

# objek2 merujuk pada objek yang sama dengan objek1
objek2_2007 = objek1_2007

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_2007 = data.copy()
    
print("objek1 =",objek1_2007)
print("objek2 =", objek2_2007)
print("objek3 =",objek3_2007)

# Operator is
hasil_2007 = objek1_2007 is objek2_2007
print("\noperator identitas IS")
print("objek1 is objek2 =", hasil_2007)

# Operator is not
hasil_2007 = objek1_2007 is not objek3_2007
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_2007)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1_2007 is objek3_2007)
print("objek1 == objek3 =", objek1_2007 == objek3_2007)
