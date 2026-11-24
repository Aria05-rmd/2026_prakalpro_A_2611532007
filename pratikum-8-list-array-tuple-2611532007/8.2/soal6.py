LAST_DIGIT = 7  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below
for i in range (7):
  Day = int(input("Masukkan pengeluaran"))
  print("Day", i+1,":", Day)
  expenses.append(Day)
print(expenses)

total = 0
highest = expenses[0]
days_above_limit = 0

for expense in expenses:
  total += expense
  if expense > highest:
    highest = expense
  if expense >= daily_limit:
    days_above_limit += 1

average = total/len(expenses)

print(daily_limit)
print(total)
print(average)
print(highest)
print(days_above_limit)