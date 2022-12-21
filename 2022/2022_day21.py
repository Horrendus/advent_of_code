import operator

OPS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}

EXAMPLE_DATA = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""


def get_monkey_number(numbers, operand):
    if isinstance(operand, int):
        return operand
    elif operand in numbers:
        return numbers[operand]
    else:
        return None


def run_monkey_jobs(monkey_jobs):
    numbers = dict()
    stop_monkey = "root"
    while True:
        new_jobs = []
        for job in monkey_jobs:
            monkey = job[0]
            num1 = get_monkey_number(numbers, job[1])
            num2 = get_monkey_number(numbers, job[3])
            operation = job[2]
            if (num1 and num2) or operation == "NUMBER":
                if operation == "NUMBER":
                    numbers[monkey] = num1
                else:
                    numbers[monkey] = operation(num1, num2)
                if monkey == stop_monkey:
                    return numbers[stop_monkey]
            else:
                new_jobs.append(job)
        monkey_jobs = new_jobs


def puzzle1(monkey_jobs):
    result = run_monkey_jobs(monkey_jobs)
    print("Puzzle 1: ", result)


def puzzle2(monkey_jobs):
    pass


def parse_line(line):
    monkey = line[:4]
    operation = line[6:].split(" ")
    if len(operation) == 1:
        return monkey, int(operation[0]), "NUMBER", None
    else:
        return monkey, operation[0], OPS[operation[1]], operation[2]


def parse_input(data):
    lines = data.strip().split("\n")
    return [parse_line(line) for line in lines]


def main():
    with open("input/input_day21.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
