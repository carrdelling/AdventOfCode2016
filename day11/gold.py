
def solve(data):

    # don't care about generators, microchips or their types; just count them
    machines = [sum(d) for d in data]
    machines[0] += 4  # elerium and dilithium pairs
    steps = 0

    # move everything from each floor one space up in each iteration
    for floor in range(3):
        steps += 2 * (machines[floor] - 1) - 1
        machines[floor + 1] += machines[floor]
        machines[floor] = 0

    return steps


def main():

    data = []
    with open('input') as in_f:
        for row in in_f:
            data.append((row.count('generator'), row.count('microchip')))

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
