import hashlib
from itertools import groupby


def solve(data):

    keys = []

    test = 0

    secrets = {}

    while len(keys) < 64:

        message = f'{data}{test}'

        if message not in secrets:
            secrets[message] = hashlib.md5(message.encode()).hexdigest()

        # find candidate
        candidate = None
        # print(secrets[message],message, test)
        for label, group in groupby(secrets[message]):
            size = sum(1 for _ in group)
            if size >= 3:
                candidate = str(label) * 5
                break

        # search for matching secrets
        if candidate is not None:
            tries = 1000

            for t in range(1, tries+1):

                message = f'{data}{test+t}'

                if message not in secrets:
                    secrets[message] = hashlib.md5(message.encode()).hexdigest()

                if candidate in str(secrets[message]):
                    keys.append(test)
                    break
        # end test
        test += 1

    solution = keys[-1]

    return solution


def main():

    with open('input') as in_f:
        data = in_f.readline().strip()

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
