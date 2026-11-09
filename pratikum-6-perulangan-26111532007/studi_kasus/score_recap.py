PASS_SCORE = 65

n = int(input("Number of students: "))

while n < 1:
    print("Invalid student count!")
    n = int(input("Number of students: "))

total = 0
lolos = 0
lowest = 100

for i in range (1, 1 + n ):
    print("Student ke ", i)
    score = int(input("Enter score: "))
    
    while score < 0 or score > 100:
        print("Invalid score!")
        score = int(input("Enter score: "))

    total += score

    if  score >= PASS_SCORE:
        lolos += 1
    if score < lowest :
        lowest = score

average = round(total / n, 2)

print(("Total score   : ")),total
print(("Average score : ")),average
print(("lolos         : ")),lolos
print(("Lowest score  : ")),lowest