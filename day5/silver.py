from hashlib import md5


def solve(data):

    key = data[0].encode('utf-8')
    salt = 0
    pwd = []

    generator = md5()
    generator.update(key)

    while len(pwd) < 8:
        _generator = generator.copy()
        _generator.update(str(salt).encode('utf-8'))
        _hash = _generator.hexdigest()
        if _hash[:5] == '00000':
            pwd.append(_hash[5])
            print(pwd, salt)
        salt += 1

    solution = ''.join(pwd)

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
