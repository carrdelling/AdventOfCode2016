

def solve(data):

    positions = {}
    current = {}
    solution = -1

    for idx, d in enumerate(data, 1):
        positions[idx] = d[0]
        current[idx] = (d[1] + idx) % positions[idx]

    new_disk = max(positions) + 1
    positions[new_disk] = 11
    current[new_disk] = 0 + new_disk

    for i in range(9999999):

        for idx in positions:
            if ((i + current[idx]) % positions[idx]) != 0:
                break
        else:
            solution = i
            break

    return solution


def main():

    data = []
    with open('input') as in_f:
        for row in in_f:
            chunks = row.strip().split()
            case = int(chunks[3]), int(chunks[-1][:-1])

            data.append(case)

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
