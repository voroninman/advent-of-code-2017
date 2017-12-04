import sys


up = lambda point: (point[0], point[1] - 1)
down = lambda point: (point[0], point[1] + 1)
left = lambda point: (point[0] - 1, point[1])
right = lambda point: (point[0] + 1, point[1])


def path():
    n = 1
    while True:
        yield right, n
        yield up, n
        yield left, n + 1
        yield down, n + 1
        n += 2


def neighborhood_sum(matrix, point):
    neighbors = [
        up(point),
        down(point),
        left(point),
        right(point),
        up(left(point)),
        up(right(point)),
        down(left(point)),
        down(right(point)),
    ]
    return sum(matrix.get(neighbor, 0) for neighbor in neighbors)


def solve(x):
    matrix = {}
    point = (0, 0)
    matrix[point] = 1

    for move, steps in path():
        for _ in range(steps):
            point = move(point)
            matrix[point] = neighborhood_sum(matrix, point)

            if matrix[point] > x:
                return matrix[point]


print(solve(int(sys.argv[1])))
