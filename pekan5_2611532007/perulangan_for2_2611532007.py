# Perulangan for dalam python

ulang_2007 = int(input("Masukkan jumlah perulangan: "))
print("Perulangan ke-0", ulang_2007-1)
for i in range(ulang_2007):
    print(i, end=" ")
print()
print("Perulangan ke-1 sampai ke-", ulang_2007)
for i in range(1,ulang_2007+1):
    print(i,end=" ")