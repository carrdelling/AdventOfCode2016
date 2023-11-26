

def is_tls(ip):

    is_valid = False
    in_brackets = False

    buffer = []
    for c in ip:

        if c == '[' and not in_brackets:
            in_brackets = True
            buffer = []
            continue
        if c == ']' and in_brackets:
            in_brackets = False
            buffer = []
            continue

        buffer.append(c)

        pattern = ((len(buffer) > 3) and (buffer[-4] == buffer[-1])
                   and (buffer[-3] == buffer[-2]) and (buffer[-1] != buffer[-2]))

        if pattern and in_brackets:
            return False

        if pattern and not in_brackets:
            is_valid = True

    return is_valid


def solve(data):

    solution = 0
    for ip in data:
        tls = is_tls(ip)

        solution += 1 if tls else 0

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
