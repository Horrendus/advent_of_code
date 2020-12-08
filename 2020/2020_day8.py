def run_program(program):
    count = [0] * len(program)
    acc = 0
    ip = 0
    possible_errors = []
    while True:
        count[ip] += 1
        instruction = program[ip]
        if instruction[0] == "nop":
            if instruction[1] != 1:
                possible_errors.append(ip)
            ip += 1
        elif instruction[0] == "acc":
            acc += instruction[1]
            ip += 1
        elif instruction[0] == "jmp":
            if instruction[1] != 1:
                possible_errors.append(ip)
            ip += instruction[1]
        if ip >= len(program):
            end_ok = True
            break
        elif count[ip] == 1:
            end_ok = False
            break

    return acc, possible_errors, end_ok


def puzzle1(program):
    acc, _, _ = run_program(program)
    print("Puzzle 1: ", acc)


def puzzle2(program):
    acc, possible_errors, end_ok = run_program(program)
    program_copy = program.copy()
    while not end_ok:
        last_error = possible_errors.pop()
        program = program_copy.copy()
        if program[last_error][0] == "nop":
            program[last_error] = ("jmp", program[last_error][1])
        elif program[last_error][0] == "jmp":
            program[last_error] = ("nop", program[last_error][1])
        acc, _, end_ok = run_program(program)
    print(f"Puzzle 2: OK: {end_ok} Acc: {acc}")


def parse_program(data):
    program = []
    for line in data:
        instruction, _, argument = line.partition(" ")
        program.append((instruction, int(argument)))
    return program


def parse_input(data):
    return data.split("\n")


def main():
    with open("input/input_day8.txt") as f:
        data = f.read()
    data = parse_input(data)
    program = parse_program(data)
    puzzle1(program)
    puzzle2(program)


if __name__ == "__main__":
    main()
