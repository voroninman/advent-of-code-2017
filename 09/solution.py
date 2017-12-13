nesting = 0
score = 0
in_garbage = False
skip_next = False
garbage_count = 0

with open('input') as f:
    input_ = f.read().strip()

for char in input_:
    if char == '!' or skip_next:
        skip_next = not skip_next
        continue

    if in_garbage:
        if char == '>':
            in_garbage = False
        else:
            garbage_count += 1
        continue

    if char == '<':
        in_garbage = True

    if char == '{':
        nesting += 1

    if char == '}':
        score += nesting
        nesting -= 1

print(score, garbage_count)
