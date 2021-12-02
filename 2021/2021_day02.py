def puzzle1(data):
    depth = 0
    pos = 0
    for instruction in data:
        if instruction[0] == "down":
            depth = depth + instruction[1]
        elif instruction[0] == "up":
            depth = max(depth - instruction[1], 0)
        elif instruction[0] == "forward":
            pos = pos + instruction[1]
    print(f"Puzzle 1: Depth: {depth}, Pos: {pos}, Result: {depth*pos}")


def puzzle2(data):
    depth = 0
    pos = 0
    aim = 0
    for instruction in data:
        if instruction[0] == "down":
            aim = aim + instruction[1]
        elif instruction[0] == "up":
            aim = max(aim - instruction[1], 0)
        elif instruction[0] == "forward":
            pos = pos + instruction[1]
            depth = depth + aim * instruction[1]

    print(f"Puzzle 2: Depth: {depth}, Pos: {pos}, Aim: {aim} Result: {depth * pos}")


def parse_input(data):
    return [(line.split(" ")[0], int(line.split(" ")[1])) for line in data.strip().split("\n")]


def main():
    with open("input/input_day02.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
