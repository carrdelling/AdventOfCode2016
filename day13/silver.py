from collections import Counter
from functools import partial
import heapq


def is_wall(x, y, signature):

    a = x * x + 3 * x + 2 * x * y + y + y * y
    a += signature

    return Counter(str(bin(a)))['1'] % 2 == 1


def moves(x, y):

    yield x + 1, y
    yield x, y + 1

    if x > 0:
        yield x - 1, y
    if y > 0:
        yield x, y - 1


def solve(designer):

    start = 1, 1
    target = 31, 39

    explore = partial(is_wall, signature=designer)

    building = {start: explore(*start)}
    best = {}

    states = [(0, start)]

    while len(states) > 0:

        current = heapq.heappop(states)
        cost, pos = current

        # are we there yet?
        if pos == target:
            continue

        # are we faster than the best so far?
        for move in moves(*pos):

            if move not in building:
                building[move] = explore(*move)

            # this is a wall
            if building[move]:
                continue

            # would this be too expensive?
            if best.get(move, 9E99) > cost + 1:
                best[move] = cost + 1
                new_state = (cost + 1, move)
                heapq.heappush(states, new_state)

    solution = best[target]

    return solution


def main():

    with open('input') as in_f:
        data = int(in_f.readline().strip())

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
