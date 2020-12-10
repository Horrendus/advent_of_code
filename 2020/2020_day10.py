def puzzle1(data):
    one_j_diff = 0
    two_j_diff = 0
    three_j_diff = 0
    data.sort()
    current = 0
    for adapter in data:
        diff = adapter - current
        if diff < 1 or diff > 3:
            break
        elif diff == 1:
            one_j_diff += 1
        elif diff == 2:
            two_j_diff += 1
        elif diff == 3:
            three_j_diff += 1
        current = adapter
    out = adapter + 3
    three_j_diff += 1
    print("Puzzle 1: ", one_j_diff*three_j_diff)


def puzzle2(data):
    pass


def parse_input(data):
    return list(map(int, data.split("\n")))


def main():
    with open("input/input_day10.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
