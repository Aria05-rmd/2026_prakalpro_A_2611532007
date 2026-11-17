full_name = "Aria ramadhan"
nim = "2611532007"
name = full_name.lower().strip()
spasi = name.find(" ")
first_name = " "

if spasi == -1:
  first_name = name
else:
  first_name = name[:spasi]
username = first_name + nim[-3:]

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print("Name".ljust(10),":",name.title())
print("NIM".ljust(10),":",nim)
print("Username".ljust(10),":",username)
print("Intake".ljust(10),":","20" + nim[:2])
print("="*30)