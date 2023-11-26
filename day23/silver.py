
def solve(data):

    memory = {
        'a': 7,  # eggs!
        'b': 0,
        'c': 1,
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
                if ins[2] in memory:
                    ip += memory[ins[2]]
                else:
                    ip += int(ins[2])
                ip -= 1   # offset the usual increment

        if ins[0] == 'tgl':
            if ins[1] in memory:
                t_value = memory[ins[1]]
            else:
                t_value = int(ins[1])

            target = ip + t_value

            no_op = False
            if target < 0:
                no_op = True
            if target >= len(data):
                no_op = True

            if no_op:
                pass
            elif data[target][0] == 'inc':
                data[target][0] = 'dec'
            elif data[target][0] in {'dec', 'tgl'}:
                data[target][0] = 'inc'
            elif data[target][0] == 'jnz':
                data[target][0] = 'cpy'
            else:
                data[target][0] = 'jnz'

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
