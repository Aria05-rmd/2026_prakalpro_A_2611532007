# Buat file dengan nama multi_if1.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_2007 =int(input("Input umur anda:"))
sim = input("Apakah Anda Sudah Punya Sim C(y/t):")[0]

if umur_2007 >= 17 and sim =='y':
    print("Anda Sudah dewasa dan boleh bawa motor")

if umur_2007 >= 17 and sim !='y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

if umur_2007 < 17 and sim !='y':
    print("Anda Belum Cukup Umur bawa motor")

if umur_2007 < 17 and sim =='y':
    print("Anda Belum Cukup Umur punya SIM")