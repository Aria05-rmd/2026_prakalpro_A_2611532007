# Buat file dengan nama Konstanta_2611532007.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variable ditambah 4 digit nim terakhir contoh: jari_1234

from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_2007 = float(input('Masukkan nilai jari-jari: '))
luas_2007 = PI * jari_2007 * jari_2007
print("Luas lingkaran dengan jari jari %.2f adalah %.2f" % (jari_2007, luas_2007))