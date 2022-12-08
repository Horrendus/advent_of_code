def calculate_visibilities_row(range_x, trees, visible_trees):
    for y in range(len(trees)):
        max_tree = -1
        for x in range_x:
            tree = trees[y][x]
            if tree > max_tree:
                visible_trees[y][x] = 1
                max_tree = tree
                if tree == 9:
                    break


def calculate_visibilities_col(range_y, trees, visible_trees):
    for x in range(len(trees)):
        max_tree = -1
        for y in range_y:
            tree = trees[y][x]
            if tree > max_tree:
                visible_trees[y][x] = 1
                max_tree = tree
                if tree == 9:
                    break


def puzzle1(trees):
    visible_trees = [[0 for _ in range(len(trees))] for _ in range(len(trees))]
    # rows from left
    calculate_visibilities_row(range(len(trees)), trees, visible_trees)
    # rows from right
    calculate_visibilities_row(range(len(trees) - 1, -1, -1), trees, visible_trees)
    # cols from up
    calculate_visibilities_col(range(len(trees)), trees, visible_trees)
    # cols from down
    calculate_visibilities_col(range(len(trees) - 1, -1, -1), trees, visible_trees)
    visible_count = sum([sum(row) for row in visible_trees])
    print("Puzzle 1: ", visible_count)


def calculate_viewing_distance_row(range_x, y, max_tree_size, trees):
    distance = 0
    for x in range_x:
        tree = trees[y][x]
        distance += 1
        if tree >= max_tree_size:
            break
    return distance


def calculate_viewing_distance_col(x, range_y, max_tree_size, trees):
    distance = 0
    for y in range_y:
        tree = trees[y][x]
        distance += 1
        if tree >= max_tree_size:
            break
    return distance


def calculate_viewing_distance(x, y, trees, viewing_distance):
    tree = trees[y][x]
    distance = calculate_viewing_distance_row(range(x + 1, len(trees)), y, tree, trees)
    distance *= calculate_viewing_distance_row(
        range(x - 1, -1, -1),
        y,
        tree,
        trees,
    )
    distance *= calculate_viewing_distance_col(x, range(y + 1, len(trees)), tree, trees)
    distance *= calculate_viewing_distance_col(x, range(y - 1, -1, -1), tree, trees)
    viewing_distance[y][x] = distance


def puzzle2(trees):
    viewing_distance = [[0 for _ in range(len(trees))] for _ in range(len(trees))]
    for x in range(len(trees)):
        for y in range(len(trees)):
            calculate_viewing_distance(x, y, trees, viewing_distance)
    max_viewing_distance = max([max(row) for row in viewing_distance])
    print("Puzzle 2: ", max_viewing_distance)


def parse_input(data):
    tree_lines = data.strip().split("\n")
    trees = [[int(tree) for tree in tree_line] for tree_line in tree_lines]
    return trees


def main():
    with open("input/input_day08.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
