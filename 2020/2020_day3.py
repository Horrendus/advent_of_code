import math


def check_slope(data, x_diff, y_diff):
    position = (0, 0)
    tree_count = 0
    line_length = len(data[0])
    while position[1] < (len(data)-1):
        x_new = (position[0] + x_diff) % line_length
        y_new = position[1] + y_diff
        position = (x_new, y_new)
        if data[position[1]][position[0]] == '#':
            tree_count += 1
    return tree_count


def puzzle1(data):
    tree_count = check_slope(data, 3, 1)
    print("Trees (Slope 3,1): ", tree_count)


def puzzle2(data):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_counts = []
    for slope in slopes:
        tree_count = check_slope(data, slope[0], slope[1])
        tree_counts.append(tree_count)
    print("Trees per Slope: ", tree_counts)
    print("Tree counts multiplied: ", math.prod(tree_counts))


def parse_input(data):
    return data.split("\n")


def main():
    with open("input/input_day3.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
