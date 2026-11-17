text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

text = "Aria ramadhan"
count = 0
for char in text.lower():
    if char in "aiueo":
        count += 1
print("Vowels:", count)