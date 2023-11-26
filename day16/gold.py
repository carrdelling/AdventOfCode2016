
def solve(data):

    a = data
    disk = 35651584

    while len(a) < disk:
        b = ''.join([{'1': '0', '0': '1'}[c] for c in a[::-1]])
        a = a + '0' + b

    checksum = a[:disk]

    while len(checksum) % 2 == 0:
        new_checksum = []
        for p in range(0, len(checksum), 2):
            if checksum[p] == checksum[p+1]:
                new_checksum.append('1')
            else:
                new_checksum.append('0')

        checksum = ''.join(new_checksum)

    solution = checksum

    return solution


def main():

    with open('input') as in_f:
        data = in_f.readline().strip()

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
