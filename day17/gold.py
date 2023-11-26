import hashlib
from collections import deque


def moves(x, y, keys):

    if x < 3 and keys[1] in {'b', 'c', 'd', 'e', 'f'}:
        yield x+1, y, 'D'
    if x > 0 and keys[0] in {'b', 'c', 'd', 'e', 'f'}:
        yield x-1, y, 'U'
    if y > 0 and keys[2] in {'b', 'c', 'd', 'e', 'f'}:
        yield x, y-1, 'L'
    if y < 3 and keys[3] in {'b', 'c', 'd', 'e', 'f'}:
        yield x, y+1, 'R'


def solve(data):

    current = 0, 0
    goal = 3, 3

    options = deque()
    options.append((current, data))

    solution = ''
    while len(options) > 0:

        pos, path = options.popleft()
        if pos == goal:
            if len(path) > len(solution):
                solution = path
                continue
            continue

        keys = list(hashlib.md5(path.encode()).hexdigest()[:4])

        for x, y, d in moves(*pos, list(keys)):
            new_state = (x, y), path + d
            options.append(new_state)

    return len(solution.replace(data, ''))


def main():

    with open('input') as in_f:
        data = in_f.readline().strip()

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
