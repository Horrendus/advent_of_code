def run_program(program):
    current_pos = 0

    while True:
        opcode = program[current_pos]
        if opcode == 99:
            break
        operand1 = program[program[current_pos + 1]]
        operand2 = program[program[current_pos + 2]]
        output_position = program[current_pos + 3]
        if opcode == 1:
            result = operand1 + operand2
        if opcode == 2:
            result = operand1 * operand2
        program[output_position] = result
        current_pos += 4
    return program


def puzzle1(program):
    program[1] = 12
    program[2] = 2
    result = run_program(program)

    print("Puzzle 1:", result[0])


def puzzle2(program):
    original_program = program.copy()
    for i in range(100):
        for j in range(100):
            program[1] = i
            program[2] = j
            result = run_program(program)
            if result[0] == 19690720:
                print("Puzzle 2: ", i, j, 100 * i + j)
                return
            program = original_program.copy()


def main():
    with open("input/input_day2.txt") as f:
        data = f.read()
    program = [int(s.strip()) for s in data.split(",")]
    original_program = program.copy()
    puzzle1(program)
    puzzle2(original_program)


if __name__ == "__main__":
    main()
