
def solve(data):

    memory = {
        'a': 0,
        'b': 0,
        'c': 1,  # gold level
        'd': 0,
    }

    ip = 0

    while ip < len(data):
        ins = data[ip]

        if ins[0] == 'inc':
            memory[ins[1]] += 1
        if ins[0] == 'dec':
            memory[ins[1]] -= 1

        if ins[0] == 'cpy':

            if ins[1] in memory:
                memory[ins[2]] = memory[ins[1]]
            else:
                memory[ins[2]] = int(ins[1])

        if ins[0] == 'jnz':
            if ins[1] in memory:
                test = memory[ins[1]] != 0
            else:
                test = int(ins[1]) != 0

            if test:
                ip += int(ins[2])
                ip -= 1   # offset the usual increment

        ip += 1

    solution = memory['a']

    return solution


def main():

    data = []
    with open('input') as in_f:
        for row in in_f:
            data.append(row.split())

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
