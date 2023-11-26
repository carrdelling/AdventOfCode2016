from hashlib import md5


def solve(data):

    key = data[0].encode('utf-8')
    salt = 0
    pwd = ['-1'] * 8

    generator = md5()
    generator.update(key)

    while '-1' in pwd:
        _generator = generator.copy()
        _generator.update(str(salt).encode('utf-8'))
        _hash = _generator.hexdigest()
        if _hash[:5] == '00000':
            pos = int(_hash[5], 16)
            if pos < 8 and pwd[pos] == '-1':
                pwd[pos] = _hash[6]
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
