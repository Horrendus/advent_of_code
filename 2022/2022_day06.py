def find_marker(data, marker_length):
    for i in range(len(data) - marker_length + 1):
        if len(set(data[i : i + marker_length])) == marker_length:
            return i + marker_length
    return -1


def puzzle1(data):
    print("Puzzle 1: ", find_marker(data, 4))


def puzzle2(data):
    print("Puzzle 1: ", find_marker(data, 14))


def parse_input(data):
    return data.strip()


def main():
    with open("input/input_day06.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
