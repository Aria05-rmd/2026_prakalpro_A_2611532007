# Manual
tinggi_2007 = int(input("Masukkan tinggi segitiga: "))

for i_2007 in range(1, tinggi_2007 + 1):
    print(" " * (tinggi_2007 - i_2007), "* " * i_2007)


# Compare with AI

# Meminta input tinggi segitiga dari pengguna
tinggi = int(input("Masukkan tinggi segitiga: "))

print("\n--- Segitiga Sama Kaki ---")
# Perulangan untuk mencetak baris
for i in range(1, tinggi + 1):
    # Menghitung jumlah spasi (semakin ke bawah semakin sedikit)
    spasi = " " * (tinggi - i)
    
    # Menghitung jumlah bintang (rumus ganjil: 1, 3, 5, 7...)
    bintang = "*" * (2 * i - 1)
    
    # Mencetak gabungan spasi dan bintang
    print(spasi + bintang)
