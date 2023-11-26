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

    solution = None
    while solution is None:

        pos, path = options.popleft()
        print(pos, path)
        if pos == goal:
            solution = path.replace(data, '')
            continue

        keys = list(hashlib.md5(path.encode()).hexdigest()[:4])

        for x, y, d in moves(*pos, list(keys)):
            new_state = (x, y), path + d
            options.append(new_state)

    return solution


def main():

    with open('input') as in_f:
        data = in_f.readline().strip()

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
