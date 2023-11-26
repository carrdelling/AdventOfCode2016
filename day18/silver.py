from collections import Counter


def solve(data):

    maze = {}
    rows = 40

    for idx, s in enumerate(data):
        maze[0, idx] = s

    for r in range(1, rows):
        for c in range(len(data)):

            maze[r, c] = {
                ('^', '^', '.'): '^',
                ('.', '^', '^'): '^',
                ('^', '.', '.'): '^',
                ('.', '.', '^'): '^',
            }.get((maze.get((r-1, c-1), '.'),
                   maze.get((r-1, c), '.'),
                   maze.get((r-1, c+1), '.'),
                   ), '.')

    solution = Counter(maze.values())['.']

    return solution


def main():

    with open('input') as in_f:
        data = in_f.readline().strip()

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
