username = input("Enter your username: ")

while len(username) >= 5:
    if len(username) < 5:
        print("Username must be at least 5 characters long.")
        username = input("Enter your username: ")
