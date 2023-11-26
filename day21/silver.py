

def rotate_left(x, s):
    left, right = s[:x], s[x:]
    return right + left


def rotate_right(x, s):
    left, right = s[:-x], s[-x:]
    return right + left


def swap_position(x, y, s):
    p = list(s)
    p[x], p[y] = p[y], p[x]
    return ''.join(p)


def swap_letter(x, y, s):
    return ''.join([{x: y, y: x}.get(c, c) for c in s])


def reverse(x, y, s):
    return s[:x] + s[x:y+1][::-1] + s[y+1:]


def move(x, y, s):
    c = s[x]
    s = s[:x] + s[x+1:]
    return s[:y] + c + s[y:]


def solve(data):

    password = 'abcdefgh'

    for ins in data:
        chunks = ins.split()

        if chunks[0] == 'reverse':

            x, y = int(chunks[2]), int(chunks[4])
            password = reverse(x, y, password)

        if chunks[0] == 'swap' and chunks[1] == 'position':

            x, y = int(chunks[2]), int(chunks[5])
            password = swap_position(x, y, password)

        if chunks[0] == 'swap' and chunks[1] == 'letter':

            x, y = chunks[2], chunks[5]
            password = swap_letter(x, y, password)

        if chunks[0] == 'rotate' and chunks[1] == 'left':

            x = int(chunks[2])
            password = rotate_left(x, password)

        if chunks[0] == 'rotate' and chunks[1] == 'right':

            x = int(chunks[2])
            password = rotate_right(x, password)

        if chunks[0] == 'rotate' and chunks[1] == 'based':

            x = chunks[-1]
            idx = password.find(x)
            steps = idx + 2 if idx >= 4 else idx + 1
            steps = steps % len(password)
            password = rotate_right(steps, password)

        if chunks[0] == 'move':

            x, y = int(chunks[2]), int(chunks[5])
            password = move(x, y, password)

    solution = password

    return solution


def main():

    with open('input') as in_f:
        data = [r for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()