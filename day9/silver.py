

def solve(data):

    deflated = []

    buffer = []
    in_pattern = False

    for c in data:
        if in_pattern:
            if c == ')':
                # compute pattern
                if 'x' in buffer:
                    size, repeat = map(int, ''.join(buffer).split('x'))

                    batch = [next(data) for _ in range(size)]

                    for _ in range(repeat):
                        deflated += list(batch)

                else:
                    deflated += buffer
                in_pattern = False
                buffer = []
                continue
            if c == '(':
                deflated += buffer
                buffer = []
                continue
            buffer.append(c)
        else:
            if c == '(':
                buffer = []
                in_pattern = True
                continue
            else:
                deflated.append(c)

    solution = len(deflated)

    return solution


def main():

    with open('input') as in_f:
        for row in in_f:
            data = (c for c in row.strip())

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
