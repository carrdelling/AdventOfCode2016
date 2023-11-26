from collections import defaultdict


def solve(data):

    inputs = defaultdict(list)
    outputs = defaultdict(int)

    done = set()
    for row in data:

        if ' goes ' in row:
            v = int(row.split(' ')[1])
            bot = int(row.split(' ')[-1])

            inputs[bot].append(v)

            done.add(row)

    solution = -1
    while len(done) < len(data):

        for row in data:
            if row in done:
                continue

            chunks = row.split(' ')
            bot_id = int(chunks[1])

            if len(inputs[bot_id]) == 2:
                low, high = min(inputs[bot_id]), max(inputs[bot_id])

                if low == 17 and high == 61:
                    solution = bot_id

                is_output = chunks[5] == 'output'

                if is_output:
                    outputs[int(chunks[6])] = low
                else:
                    inputs[int(chunks[6])].append(low)

                is_output = chunks[10] == 'output'

                if is_output:
                    outputs[int(chunks[11])] = high
                else:
                    inputs[int(chunks[11])].append(high)

                done.add(row)

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
