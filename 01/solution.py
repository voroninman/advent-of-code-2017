from functools import reduce
from typing import List


def prepare(text: str) -> List[int]:
    """Convert input into appropriate data structure."""
    return list(map(int, text.strip()))


def solve(data: List[int], step=1) -> int:
    rv = 0
    for i in range(len(data)):
        if data[i - step] == data[i]:
            rv += data[i]
    return rv


with open('input') as f:
    input_ = f.read()

data = prepare(input_)
solution1 = solve(data, step=1)
solution2 = solve(data, step=len(data) // 2)

print(solution1, solution2)
