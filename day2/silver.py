

def solve(data):

    output = []

    current = 5
    for d in data:

        for v in d:

            if v == 'U':
                current -= 3 if current > 3 else 0
            if v == 'D':
                current += 3 if current < 7 else 0
            if v == 'L':
                current -= 1 if (current % 3) != 1 else 0
            if v == 'R':
                current += 1 if (current % 3) != 0 else 0

        output.append(current)

    solution = ''.join(map(str, output))

    return solution


def main():

    data = []
    with open('input') as in_f:
        for row in in_f:
            seq = [c for c in row.strip()]
            data.append(seq)

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
