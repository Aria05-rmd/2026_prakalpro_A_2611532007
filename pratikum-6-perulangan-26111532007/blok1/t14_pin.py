attempt_2007 = 1
MAX_ATTEMPS_2007 = 3
correct_pin_2007 = "1234"
pin_2007 = input("Enter PIN: ")


while pin_2007 != correct_pin_2007 and attempt_2007 < MAX_ATTEMPS_2007:
    print("Incorrect PIN.")
    pin_2007 = input("Enter PIN: ")
    attempt_2007 += 1

if pin_2007 == correct_pin_2007:
    print("Access granted")
else:
    print("Account locked")

        

