from collections import Counter, defaultdict


def solve(data):

    counts = defaultdict(lambda: Counter())

    for w in data:
        for idx, c in enumerate(w):
            counts[idx][c] += 1

    solution = ''.join([counter.most_common(1)[0][0] for idx, counter in sorted(counts.items())])

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
