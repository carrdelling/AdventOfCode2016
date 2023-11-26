

def solve(data):

    possible = sum(1 if (sum(d) - max(d)) > max(d) else 0 for d in data)

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
