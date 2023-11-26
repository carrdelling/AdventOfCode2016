

def solve(data):

    output = []

    current = 5
    for d in data:

        for v in d:

            if v == 'U':
                if current == 3:
                    current = 1
                elif current in {6, 7, 8}:
                    current -= 4
                elif current in {10, 11, 12}:
                    current -= 4
                elif current == 13:
                    current = 11
                else:
                    pass
            if v == 'D':
                if current == 1:
                    current = 3
                elif current in {2, 3, 4}:
                    current += 4
                elif current in {6, 7, 8}:
                    current += 4
                elif current == 11:
                    current = 13
                else:
                    pass
            if v == 'L':
                if current not in {1, 2, 5, 10, 13}:
                    current -= 1
                else:
                    pass
            if v == 'R':
                if current not in {1, 4, 9, 12, 13}:
                    current += 1

        output.append(str({10: 'A', 11: 'B', 12:'C', 'D': 13}.get(current, current)))

    solution = ''.join(output)

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
