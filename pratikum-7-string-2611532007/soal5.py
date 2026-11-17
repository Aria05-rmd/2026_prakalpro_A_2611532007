# Name: Aria Ramadhan
# NIM: 2611532007
# Question 5

# Check the rules in a safe order and print the first rule that fails.
# Messages:
#   "Invalid: at least 5 characters"
#   "Invalid: letters and digits only"
#   "Invalid: must start with a letter"
#   "Valid"

username = input("Username: ")
if not username.isalnum():
  print("Invalid: must start with a letter")
elif not username[0].isalpha():
  print("Invalid: letters and digits only")
elif len(username) < 5:
  print("Invalid: at least 5 characters")
else:
  print("Valid")

nim =  input("NIM :")

if not nim.isalnum():
  print("Invalid NIM")
elif len(nim) != 10:
  print("Invalid NIM")
else:
  print("Valid") 
  nimbaru = "x" * 2 + nim[3:]
  print(nimbaru)