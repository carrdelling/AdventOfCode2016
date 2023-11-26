

def is_ssl(ip):

    inside_patterns = set()
    outside_patterns = set()

    buffer = []
    in_brackets = False
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

        if len(buffer) > 2:
            if (buffer[-3] == buffer[-1]) and (buffer[-3] != buffer[-2]):

                if in_brackets:
                    new_pattern = (buffer[-3], buffer[-2], buffer[-1])
                    inside_patterns.add(new_pattern)
                else:
                    reverse_pattern = (buffer[-2], buffer[-1], buffer[-2])
                    outside_patterns.add(reverse_pattern)

    is_valid = len(inside_patterns & outside_patterns) > 0

    return is_valid


def solve(data):

    solution = 0
    for ip in data:
        tls = is_ssl(ip)

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
