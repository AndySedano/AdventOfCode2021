import math

count = 0
prev_value = math.inf

with open(f'day1.txt', 'r') as file:
    for line in file:
        value = int(line)
        if value > prev_value:
            count += 1
        prev_value = value

print(count)
