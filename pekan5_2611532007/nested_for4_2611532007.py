# Perulangan for dalam python

tinggi_2007 = int(input("Masukkan tinggi pola (Bilangan grnap, misal 10): "))

if tinggi_2007 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_2007 = tinggi_2007
    c_2007 = a_2007
    lebar_2007 = (2 * tinggi_2007) - 2

    for i in range(1, tinggi_2007 + 1):
        b_2007 = c_2007 + 1

        for j in range(1, lebar_2007 + 1):

            # baris atas dan bawah
            if i == 1 or 1 == tinggi_2007:
                if j == 1 or j == lebar_2007:
                    print("#", end="")
                else:
                    print("=", end="")
            else:
                if j == 1 or j == lebar_2007:
                    print("|", end="")
                else:
                    if j == c_2007:
                        print("<", end=" ")
                    elif j == b_2007:
                        print(">", end=" ")
                    elif j == (lebar_2007 - c_2007):
                        print ("<", end=" ")
                    elif j == b_2007 and j < (lebar_2007 - c_2007 + 1):
                        print(">", end=" ")
                    elif j > b_2007 and j < (lebar_2007 - c_2007):
                        print(".", end=" ")
                    else:
                        print(" ", end=" ")

        print()

        # logika asli java

        if a_2007 <= 0:
            c_2007 = (-a_2007)+2
        else:
            c_2007 = a_2007
                                