def puzzle1(data):
    pixels = ""
    register_x = 1
    executing_instructions = []
    sum_signal_strength = 0
    i = 0
    cycle = 0
    executing_addx = 0
    while True:
        # Before Cycle
        cycle += 1
        if i < len(data):
            instruction = data[i][0]
            if executing_addx == 1:
                executing_addx = 2
            elif instruction == "noop":
                i += 1
            elif instruction == "addx":
                executing_instructions.append(int(data[i][1]))
                executing_addx = 1
                i += 1
        # During Cycle
        if cycle == 20 or (cycle - 20) % 40 == 0:
            sum_signal_strength += cycle * register_x
        # Drawing Pixels
        pixel_position = (cycle - 1) % 40
        if pixel_position == 0:
            pixels += "\n"
        pixel_lit = pixel_position in [register_x - 1, register_x, register_x + 1]
        if pixel_lit:
            pixels += "#"
        else:
            pixels += "."
        # After Cycle
        if len(executing_instructions) > 0 and executing_addx == 2:
            register_x += executing_instructions.pop(0)
            executing_addx = 0
        if cycle >= 240:
            # Part 2 needs 240 Cycles
            break
    print("Puzzle 1:", sum_signal_strength)
    print("Puzzle 2:")
    print(pixels)


def puzzle2(data):
    pass


def parse_input(data):
    lines = data.strip().split("\n")
    return [line.split(" ") for line in lines]


def main():
    with open("input/input_day10.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
