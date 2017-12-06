with open('input') as f:
    numbers = list(map(int, f.readline().split('\t')))

seen = []
when = []
counter = 0

i = numbers.index(max(numbers))
cycles, numbers[i] = numbers[i], 0
while True:
    cycles -= 1
    i = (i + 1) % len(numbers)
    numbers[i] += 1

    if cycles == 0:
        counter += 1

        if numbers in seen:
            break
        seen.append(numbers[:])
        when.append(counter)

        i = numbers.index(max(numbers))
        cycles, numbers[i] = numbers[i], 0

print(counter, counter - when[seen.index(numbers)])
