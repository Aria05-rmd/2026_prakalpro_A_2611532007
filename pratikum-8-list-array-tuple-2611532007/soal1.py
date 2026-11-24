screen_minutes = [205, 185, 240, 345, 250] # your data set from Table D1
limit = 240
total = 0
highest = screen_minutes[0]
heavy_days = 0
for i in range(len(screen_minutes)):
    total += screen_minutes[i]
    if screen_minutes[i] > highest:
        highest = screen_minutes[i]
    if screen_minutes[i] >= limit:
        heavy_days += 1
print(total, highest, heavy_days)
print(total / len(screen_minutes))