from itertools import product


def solve(data):

    screen = set()
    for ins in data:

        if 'rect' in ins:
            cols, rows = (int(x) for x in ins.split(' ')[-1].split('x'))

            for x, y in product(range(rows), range(cols)):
                screen.add((x, y))
            continue

        if 'row' in ins:
            chunks = ins.split(' ')
            shift = int(chunks[-1])
            row = int(chunks[-3].split('=')[-1])

            in_row = [y for x, y in screen if x == row]
            for y in in_row:
                screen.discard((row, y))
            for y in in_row:
                screen.add((row, (y + shift) % 50))
            continue

        if 'column' in ins:
            chunks = ins.split(' ')
            shift = int(chunks[-1])
            col = int(chunks[-3].split('=')[-1])

            in_col = [x for x, y in screen if y == col]
            for x in in_col:
                screen.discard((x, col))
            for x in in_col:
                screen.add(((x + shift) % 6, col))

    solution = len(screen)

    return solution


def main():

    data = []
    with open('input') as in_f:
        for row in in_f:
            data.append(row.strip())

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
