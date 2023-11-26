

def solve(data):

    possible = 0

    b0, b1, b2 = [], [], []

    for a, b, c in data:

        b0.append(a)
        b1.append(b)
        b2.append(c)

        if len(b0) == 3:
            possible += 1 if (sum(b0) - max(b0)) > max(b0) else 0
            possible += 1 if (sum(b1) - max(b1)) > max(b1) else 0
            possible += 1 if (sum(b2) - max(b2)) > max(b2) else 0

            b0, b1, b2 = [], [], []

    solution = possible

    return solution


def main():

    data = []
    with open('input') as in_f:
        for row in in_f:
            seq = []
            buffer = []
            for c in row.strip():
                if c != ' ':
                    buffer.append(c)
                elif buffer:
                    seq.append(int(''.join(buffer)))
                    buffer = []
            else:
                seq.append(int(''.join(buffer)))
            data.append(seq)

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
