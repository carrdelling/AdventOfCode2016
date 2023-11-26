
turning = {
    ('U', 'L'): 'L',
    ('U', 'R'): 'R',
    ('D', 'L'): 'R',
    ('D', 'R'): 'L',
    ('L', 'L'): 'D',
    ('L', 'R'): 'U',
    ('R', 'L'): 'U',
    ('R', 'R'): 'D'
}

deltas = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}


def solve(data):

    direction = 'U'
    current = (0, 0)

    visited = set()
    hq = None

    for ins in data:
        turn = ins[0]
        step = int(ins[1:])

        direction = turning[(direction, turn)]

        for s in range(step):
            current = current[0] + deltas[direction][0], current[1] + deltas[direction][1]

            if current in visited:
                hq = current
                break
            else:
                visited.add(current)
        if hq is not None:
            break

    solution = sum(abs(x) for x in hq)

    return solution


def main():

    with open('input') as in_f:
        data = [c for c in in_f.readline().strip().split(', ')]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
