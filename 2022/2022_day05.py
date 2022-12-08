import copy


def puzzle1(stacks, instructions):
    for ins in instructions:
        for _ in range(ins[0]):
            stacks[ins[2]].append((stacks[ins[1]].pop()))

    answer = "".join([s[-1] for s in stacks if len(stacks) > 0])
    print("Puzzle 1: ", answer)


def puzzle2(stacks, instructions):
    for ins in instructions:
        crates = []
        for _ in range(ins[0]):
            crates.append(stacks[ins[1]].pop())
        for crate in crates[::-1]:
            stacks[ins[2]].append(crate)

    answer = "".join([s[-1] for s in stacks if len(stacks) > 0])
    print("Puzzle 2: ", answer)


def parse_stacks(stacks):
    parsed_stacks = [[], [], [], [], [], [], [], [], []]
    for i in range(len(stacks) - 2, -1, -1):
        line = stacks[i].ljust(35)
        for j in range(len(parsed_stacks)):
            pos = 1 + j * 4
            val = line[pos]
            if val != " ":
                parsed_stacks[j].append(val)

    return parsed_stacks


def parse_instructions(instructions):
    parsed_instructions = []
    for line in instructions:
        splitted_line = line[5:].split(" ")
        parsed_instructions.append(
            (
                int(splitted_line[0]),
                int(splitted_line[2]) - 1,
                int(splitted_line[4]) - 1,
            )
        )
    return parsed_instructions


def parse_input(data):
    parts = data.split("\n\n")
    stacks = parts[0].split("\n")
    instructions = parts[1].strip().split("\n")
    parsed_stacks = parse_stacks(stacks)
    parsed_instructions = parse_instructions(instructions)
    return parsed_stacks, parsed_instructions


def main():
    with open("input/input_day05.txt") as f:
        data = f.read()
    stacks, instructions = parse_input(data)
    stacks1 = copy.deepcopy(stacks)
    puzzle1(stacks1, instructions)
    puzzle2(stacks, instructions)


if __name__ == "__main__":
    main()
