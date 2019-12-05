def parse_opcode(opcode):
    opcode = str(opcode).zfill(5)
    opcode_list = [int(code) for code in list(opcode)]
    last = opcode_list.pop()
    second_last = opcode_list.pop()
    opcode_list.append(second_last * 10 + last)
    return opcode_list


def run_program(program):
    current_pos = 0
    while True:
        opcode = program[current_pos]
        if opcode == 99:
            break
        opcode_list = parse_opcode(opcode)
        opcode_op = opcode_list[3]
        param_mode_1 = opcode_list[2]
        param_mode_2 = opcode_list[1]
        param_mode_3 = opcode_list[0]
        if opcode_op == 3:
            num = input("Input: ")
            operand1 = program[current_pos + 1]
            program[operand1] = int(num)
            current_pos += 2
        if opcode_op == 4:
            operand1 = program[current_pos + 1]
            if param_mode_1 == 0:
                operand1 = program[operand1]
            print(operand1)
            current_pos += 2
        if opcode_op == 1 or opcode_op == 2:
            operand1 = program[current_pos + 1]
            if param_mode_1 == 0:
                operand1 = program[operand1]
            operand2 = program[current_pos + 2]
            if param_mode_2 == 0:
                operand2 = program[operand2]
            operand3 = program[current_pos + 3]
            if opcode_op == 1:
                result = operand1 + operand2
            if opcode_op == 2:
                result = operand1 * operand2
            program[operand3] = result
            current_pos += 4
        if opcode_op == 5 or opcode_op == 6:
            operand1 = program[current_pos + 1]
            if param_mode_1 == 0:
                operand1 = program[operand1]
            operand2 = program[current_pos + 2]
            if param_mode_2 == 0:
                operand2 = program[operand2]
            if (opcode_op == 5 and operand1 != 0) or (opcode_op == 6 and operand1 == 0):
                current_pos = operand2
            else:
                current_pos += 3
        if opcode_op == 7 or opcode_op == 8:
            operand1 = program[current_pos + 1]
            if param_mode_1 == 0:
                operand1 = program[operand1]
            operand2 = program[current_pos + 2]
            if param_mode_2 == 0:
                operand2 = program[operand2]
            operand3 = program[current_pos + 3]
            result = int(
                (opcode_op == 7 and operand1 < operand2)
                or (opcode_op == 8 and operand1 == operand2)
            )
            program[operand3] = result
            current_pos += 4

    return program


def puzzle1(program):
    run_program(program)


def puzzle2(data):
    pass


def main():
    with open("input/input_day5.txt") as f:
        data = f.read()
    program = [int(s.strip()) for s in data.split(",")]
    original_program = program.copy()
    # print(program)
    puzzle1(program)
    puzzle2(data)


if __name__ == "__main__":
    main()
