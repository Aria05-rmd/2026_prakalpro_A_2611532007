# PROGRAN JAM PASIR KRISTAL PALINDROMIK
N_2007 = int(input("Masukkan Nilai N: "))

print(" _______________________________________________ ")
print("|                                               |")
print("|==== PROGRAM JAM PASIR KRISTAL PALINDROMIK ====|")
print("|_______________________________________________|\n")
  
lebar_2007 = (4 * N_2007 + 5)

# Bingkai atas

print("#", end="")
for b_atas_2007 in range(lebar_2007):
  print("=", end="")
print("#")
    
poros_kristal_2007 = "<*>"

# Sisi atas
for i_2007 in range(N_2007,0,-1):
  print("|",end=" ")
  for spasi_kiri_2007 in range(N_2007-i_2007):
    print(" ",end=" ")
  for deret_kiri_2007 in range(i_2007,0,-1):
    print(deret_kiri_2007,end=" ")
  print(poros_kristal_2007,end=" ")
  for deret_kanan_2007 in range(1,i_2007 + 1):
    print(deret_kanan_2007,end=" ")
  for spasi_kanan_2007 in range(N_2007-i_2007):
    print(" ",end=" ")
  print("|")
      
    # Sisi Tengah
print("|",end=" ")
for spasi_kiri_2007 in range(1,N_2007+1):
  print(" ",end=" ")
print(poros_kristal_2007,end=" ")
for spasi_kanan_2007 in range(1,N_2007+1):
  print(" ",end=" ")
print("|")

# Sisi Bawah
for i_2007 in range(1,N_2007+1):
  print("|",end=" ")
  for spasi_kiri_2007 in range(N_2007-i_2007):
    print(" ",end=" ")
  for deret_kiri_2007 in range(i_2007,0,-1):
    print(deret_kiri_2007,end=" ")
  print(poros_kristal_2007,end=" ")
  for deret_kanan_2007 in range(1,i_2007+1):
    print(deret_kanan_2007,end=" ")
  for spasi_kanan_2007 in range(N_2007-i_2007):
    print(" ",end=" ")
  print("|")

# Bingka bawah
print("#", end="")
for b_bawah_2007 in range(lebar_2007):
  print("=", end="")
print("#")
    