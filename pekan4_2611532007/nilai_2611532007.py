# Buat file dengan nama nilai_nim.py
# Buat program untuk nested if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()
# program konversi nilai angka menjadi huruf

nilai = int(input("Inputkan nilai angka="))

if nilai >= 81:
    print("A")
elif nilai >= 70:
    print("B")
elif nilai >=60:
    print("C")
elif nilai >= 50:
    print("D")
else:
    print("E")