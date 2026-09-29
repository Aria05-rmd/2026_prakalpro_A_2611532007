# Perulangan for dalam python

batas_2007 = int(input("Masukkan nilai batas: "))
for line_2007 in range(1, batas_2007+1):
    for j_2007 in range(1, (-1 * line_2007 + batas_2007) + 1):
        print(".", end=" ")
    print(line_2007)