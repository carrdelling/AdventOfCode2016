
def solve(data):

    valid = 0
    for s, e in sorted(data):

        if valid < s:
            break

        if valid < e:
            valid = e + 1

    solution = valid

    return solution


def main():

    with open('input') as in_f:
        data = [tuple(map(int, r.strip().split('-'))) for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
