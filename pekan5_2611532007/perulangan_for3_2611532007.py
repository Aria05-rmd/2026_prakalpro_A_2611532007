# perulangan for dalam python

ulang_2007 = int(input("Masukkan jumlah perulangan: "))

jumlah_2007 = 0
for i in range(1, ulang_2007 + 1):
    print(i, end=" ")
    jumlah_2007 = jumlah_2007 + i

    if i < ulang_2007:
        print(" + ",jumlah_2007,end="")
    else:
        print(" = ", jumlah_2007,end="")
print()
print("jumlah =", jumlah_2007)
