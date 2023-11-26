from collections import deque
from itertools import permutations


def moves(x, y, grid):

    for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_point = x+move[0], y+move[1]
        if grid.get(new_point, '#') != '#':
            yield new_point


def find_paths(grid, interesting):
    target_paths = {}

    for place, target in interesting.items():

        paths = deque([[target]])
        seen = set()
        seen.add(target)

        while paths:
            curr_path = paths.popleft()
            x, y = curr_path[-1]
            if (x, y) in interesting.values() and len(curr_path) > 1:
                target_paths[(int(place), int(grid[(x, y)]))] = len(curr_path) - 1
                continue
            for new_p in moves(x, y, grid):
                if new_p not in seen:
                    paths.append(curr_path + [new_p])
                    seen.add(new_p)

    return target_paths


def solve(data):

    grid = {}
    interesting = {}
    for x, row in enumerate(data):
        for y, c in enumerate(row):
            grid[(x, y)] = c

            if c.isdigit():
                interesting[c] = (x, y)

    # get all minimum distances between points of interest
    target_paths = find_paths(grid, interesting)

    # get the minimum path to visit all
    min_dist = None
    for path in permutations(range(1, 8)):
        path = [0] + list(path) + [0]
        distance = 0
        for i in range(len(path) - 1):
            distance += target_paths[(path[i], path[i + 1])]

        if min_dist is None:
            min_dist = distance
        else:
            min_dist = min(min_dist, distance)

    solution = min_dist

    return solution


def main():

    data = []
    with open('input') as in_f:
        for row in in_f:
            data.append(row)

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
