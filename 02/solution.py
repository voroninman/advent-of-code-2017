from itertools import combinations
from sys import maxsize
from functools import reduce
from typing import List, Callable


def prepare(text: str) -> List[List[int]]:
    """Convert input into appropriate data structure."""
    lines = filter(None, text.split('\n'))
    return list(map(lambda line: list(map(int, line.strip().split('\t'))), lines))


def max_min_diff(numbers: List[int]) -> int:
    """
    Return the difference between maximum and minimum values from a sequence
    of numbers.

    >>> max_min_diff([5, 1, 9, 5])
    8
    >>> max_min_diff([7, 5, 3])
    4
    >>> max_min_diff([2, 4, 6, 8])
    6
    """
    max_, min_ = reduce(
        lambda acc, n: (max(n, acc[0]), min(n, acc[1])),
        numbers,
        (-maxsize, maxsize))
    return max_ - min_


def evenly_divide(numbers: List[int]) -> int:
    """
    Return division of any two numbers from the list that are evenly
    dividable.

    >>> evenly_divide([5, 9, 2, 8])
    4
    >>> evenly_divide([9, 4, 7, 3])
    3
    >>> evenly_divide([3, 8, 6, 5])
    2
    """
    for a, b in combinations(numbers, 2):
        if a % b == 0:
            return a // b
        if b % a == 0:
            return b // a
    return 0


def solve(data: List[List[int]], strategy: Callable[[List[int]], int]) -> int:
    return sum(map(strategy, data))


with open('input') as f:
    input_ = f.read()

data = prepare(input_)
solution1 = solve(data, strategy=max_min_diff)
solution2 = solve(data, strategy=evenly_divide)

print(solution1, solution2)
