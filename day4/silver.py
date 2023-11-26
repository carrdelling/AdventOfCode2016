from collections import Counter


def solve(data):

    possible = 0
    for n, checksum in data:
        chunks = n.split('-')
        name = ''.join(chunks[:-1])

        key = [a[0] for a in sorted(Counter(name).items(), key=lambda x: (-x[1], x[0]))[:5]]
        if set(key) == set(checksum):
            possible += int(chunks[-1])

    solution = possible

    return solution


def main():

    data = []
    with open('input') as in_f:
        for row in in_f:
            data.append(row.strip()[:-1].split('['))

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
