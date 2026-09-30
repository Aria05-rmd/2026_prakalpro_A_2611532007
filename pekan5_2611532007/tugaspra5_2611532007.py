
tinggi_2007 = int(input("Masukkan tinggi segitiga: "))

for i_2007 in range(1,tinggi_2007+1):
    for s_2007 in range(tinggi_2007-i_2007):
      print(" ",end="")
    for j_2007 in range (i_2007,0,-1):
      print("*",end=" ")
    print()
