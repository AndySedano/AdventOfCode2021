import math

count = 0
prev_value = math.inf

with open(f'day1.txt', 'r') as file:
    lines = [int(x) for x in file.readlines()]
    a = [x for x in lines[::]]
    b = [x for x in lines[1::]]
    c = [x for x in lines[2::]]

    for values in zip(a, b, c):
        value = sum(values)
        if value > prev_value:
            count += 1
        prev_value = value

    print(count)
