from itertools import product


def solve(data):

    nodes = {}
    for row in data:

        if row[:4] != '/dev':
            continue

        chunks = row.split()
        used = int(chunks[2].replace('T', ''))
        avail = int(chunks[3].replace('T', ''))
        node = tuple(chunks[0].split('-')[1:])

        nodes[node] = (used, avail)

    viable = 0

    for a, b in product(nodes, repeat=2):

        if a == b:
            continue
        if nodes[a][0] == 0:
            continue
        if nodes[a][0] <= nodes[b][1]:
            viable += 1

    solution = viable

    return solution


def main():

    with open('input') as in_f:
        data = [r for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()