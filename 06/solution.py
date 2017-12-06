@profile
def main():
    with open('input') as f:
        numbers = list(map(int, f.readline().split('\t')))

    seen = {}
    counter = 0

    i = numbers.index(max(numbers))
    cycles, numbers[i] = numbers[i], 0
    size = len(numbers)
    while True:
        i = (i + 1) % size
        cycles -= 1
        numbers[i] += 1

        if cycles is 0:
            counter += 1

            key = str(numbers)
            if key in seen:
                break
            seen[key] = counter

            i = numbers.index(max(numbers))
            cycles, numbers[i] = numbers[i], 0

    print(counter, counter - seen[key])


main()
