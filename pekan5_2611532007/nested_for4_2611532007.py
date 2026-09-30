tinggi_2007 = int(input("Masukkan tinggi pola (Bilangan genap, misal 10): "))

if tinggi_2007 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_2007 = tinggi_2007
    c_2007 = a_2007
    lebar_2007 = (2 * tinggi_2007) - 2

    for i in range(1, tinggi_2007 + 1):
        b_2007 = c_2007 + 1
      
        for j in range(1, lebar_2007 + 1):
            # Baris atas dan bawah
            if i == 1 or i == tinggi_2007:
                if j == 1 or j == lebar_2007:
                    print("#", end="")
                else:
                    print("=", end="")
            else:
                # Sisi kiri dan kanan (border)
                if j == 1 or j == lebar_2007:
                    print("|", end="")
                else:
                    # Logika isi pola (diamond/kristal)
                    if j == c_2007:
                        print("<", end="")
                    elif j == b_2007:
                        print(">", end="")
                    elif j == (lebar_2007 - c_2007):
                        print("<", end="")
                    elif j == (lebar_2007 - c_2007 + 1):
                        print(">", end="")
                    elif j > b_2007 and j < (lebar_2007 - c_2007):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print() # Pindah ke baris baru

        # Logika asli java (Perubahan nilai a untuk membentuk pola)
        a_2007 -= 2  # KUNCI YANG HILANG: a harus dikurangi agar pola bergerak
        
        if a_2007 <= 0:
            c_2007 = (-a_2007) + 2
        else:
            c_2007 = a_2007

                                