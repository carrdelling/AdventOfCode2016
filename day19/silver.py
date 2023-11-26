
def solve(data):

    robin = list(range(int(data)))

    while len(robin) > 1:
        drop_first = len(robin) % 2 == 1

        robin = robin[::2]
        if drop_first:
            robin = robin[1:]

    solution = robin[0] + 1

    return solution


def main():

    with open('input') as in_f:
        data = in_f.readline().strip()

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
