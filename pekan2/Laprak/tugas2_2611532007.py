# tipe data string dan char
nama_2007 = str(input("Masukkan Nama Mahasiswa: "))
jenis_kelamin_2007 = str(input('Masukkan Jenis Kelamin (L/P): '))
umur_2007 = int(input("Masukkan Umur: "))
skor_test_awal_2007 = float(input("Masukkan Skor Test Awal: "))
print("\n=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
print("Nama Mahasiswa: ", nama_2007)
print("Jenis Kelamin: ", jenis_kelamin_2007)
print("Umur: ", umur_2007)
print("Skor Tes Awal: ", skor_test_awal_2007)

#Tipe Data Numerik & Type Casting:
print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")

alamat_domisili = """
Asrama Unand
kec.pauh
kota padang
"""

print("Nama Mahasiswa : ", nama_2007, "|", "Tipe: ",type(nama_2007))
print("Jenis Kelamin: ", jenis_kelamin_2007, "|", "Tipe: ", type (jenis_kelamin_2007))
print("Alamat Domisili: ", alamat_domisili, "|", "Tipe: ", type(alamat_domisili))
print("Umur: ", umur_2007, "|", "Tipe: ", type(umur_2007))
print("Skor Tes Awal: ", skor_test_awal_2007)
ID_Sinyal_Token =  complex(3j+100)
print("ID Sinyal Token", ID_Sinyal_Token, "|", "Tipe: ",type(ID_Sinyal_Token))

#Tipe Data Boolean:
batas_minimal_skor_2007 = float(75.0)
status_kelulusan_2007 = skor_test_awal_2007 >= batas_minimal_skor_2007
print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print("apakah dinyatakan lulus?: ", status_kelulusan_2007, "|", "Tipe: ", type(status_kelulusan_2007))
