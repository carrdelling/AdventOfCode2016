from collections import deque


def solve(data):

    elves = int(data)

    # this is equivalent to balance and rotate two arrays
    left = deque(i for i in range(1, (elves // 2) + 1))
    right = deque(i for i in range(elves + 1, (elves // 2) + 1, -1))

    while left and right:
        if len(left) > len(right):
            left.pop()
        else:
            right.pop()

        # rotate
        to_right = left.popleft()
        right.appendleft(to_right)

        to_left = right.pop()
        left.append(to_left)

    return left.pop()


def main():

    with open('input') as in_f:
        data = in_f.readline().strip()

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
