import sys
from typing import Iterator


def circle_steps(n: int) -> Iterator[int]:
    curr = 2 * n
    step = -1
    while True:
        yield curr
        curr += step
        if curr == 2 * n:
            step = -1
        if curr == n:
            step = 1


def circle_maxs() -> Iterator[int]:
    n = 0
    while True:
        yield n, (2 * n + 1) ** 2
        n += 1


def solve(x: int) -> int:
    if x <= 1:
        return 0
    for n, max_ in circle_maxs():
        if x <= max_:
            steps_counter = circle_steps(n)
            for i, s in zip(range(8 * n), steps_counter):
                if max_ - i == x:
                    return s
            break


print(solve(int(sys.argv[1])))
