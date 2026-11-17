
first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())

full_name = "Aria ramadhan"
nim = "2611532007"
 
# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().
name = full_name.lower().strip()
spasi = name.find(" ")
first_name = " "

if spasi == -1:
  first_name = name
else:
  first_name = name[:spasi]

username = first_name + nim[-3:]
print(username)