with open('input') as f:
    numbers = [int(line) for line in f]

i = 0
counter = 0
x = 0
while True:
    try:
        x = numbers[i]
    except IndexError:
        break

    numbers[i], i = x + (1 if x < 3 else -1), x + i
    counter += 1

print(counter)
