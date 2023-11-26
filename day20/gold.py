
def solve(data):

    valid = 0
    count = 0
    for s, e in sorted(data):
        if valid < s:
            jump = (s - valid)
            count += jump
            valid += jump

        if valid < e:
            valid = e + 1

    if valid <= 4294967295:
        count += (4294967295 - valid) + 1

    solution = count

    return solution


def main():

    with open('input') as in_f:
        data = [tuple(map(int, r.strip().split('-'))) for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
