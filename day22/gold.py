

def print_map(nodes, max_x, max_y):

    screen = []
    for x in range(max_x + 1):
        row = []
        for y in range(max_y + 1):
            row.append(nodes.get((x, y), '#'))
        screen.append(''.join(row))

    print('\n'.join(screen))


def solve(data):

    nodes = {}
    empty_node = None
    for row in data:

        if row[:4] != '/dev':
            continue

        chunks = row.split()
        used = int(chunks[2].replace('T', ''))
        node = tuple(chunks[0].split('-')[1:])
        x, y = int(node[0][1:]), int(node[1][1:])

        if used == 0:
            nodes[(x, y)] = '*'
            empty_node = x, y
        elif 1 < used < 100:
            nodes[(x, y)] = '.'
        else:
            nodes[(x, y)] = '#'

    max_x = max(x[0] for x in nodes)
    max_y = max(x[1] for x in nodes)

    nodes[(0, 0)] = 'S'
    nodes[(max_x, 0)] = 'D'

    print_map(nodes, max_x, max_y)

    print("This is easier to solve by hand")

    wall_size = sum(1 for x in nodes.values() if x == '#')
    moves_wall_up = wall_size - (max_x - empty_node[0])
    moves_empty_to_target = empty_node[1] + wall_size + moves_wall_up

    print(f"Moves to get the empty stack to the target: {moves_empty_to_target}")

    moves_to_goal = (max_x - 1) * 5
    print("Then every move of the data back takes 5 steps")
    print(f"Moves to get to the goal: {moves_to_goal}")

    solution = moves_empty_to_target + moves_to_goal

    return solution


def main():

    with open('input') as in_f:
        data = [r for r in in_f]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
