import copy
import operator

OPS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}

EXAMPLE_DATA = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""


def do_monkey_business(monkeys, rounds, worry_level_divider):
    for round in range(rounds):
        for i in range(len(monkeys)):
            monkey = monkeys[i]
            for item in monkey["items"]:
                worry_level = monkey["operation"][0](item, monkey["operation"][1])
                worry_level = int(worry_level // worry_level_divider)
                is_divisible = (worry_level % monkey["divisible_by_test"]) == 0
                monkeys[monkey["throw"][is_divisible]]["items"].append(worry_level)
                monkey["items_inspected"] += 1
            monkey["items"] = []
        inspection_numbers = sorted(
            [m["items_inspected"] for m in monkeys], reverse=True
        )
    monkey_business = inspection_numbers[0] * inspection_numbers[1]
    return monkey_business


def puzzle1(monkeys):
    monkey_business = do_monkey_business(monkeys, 20, 3)
    print("\nPuzzle 1:", monkey_business)


def puzzle2(monkeys):
    monkey_business = do_monkey_business(monkeys, 10000, 1)
    print("\nPuzzle 2:", monkey_business)


def parse_monkey_data(monkey_data):
    monkey_data_lines = monkey_data.split("\n")
    items = [int(item) for item in monkey_data_lines[1][18:].split(", ")]
    operation = (OPS[monkey_data_lines[2][23]], monkey_data_lines[2][25:])
    if operation[1] == "old":
        # special case old * old
        operation = (operator.pow, 2)
    else:
        operation = (operation[0], int(operation[1]))
    divisible_by_test = int(monkey_data_lines[3][21:])
    if_true_throw = int(monkey_data_lines[4][29:])
    if_false_throw = int(monkey_data_lines[5][30:])
    return {
        "items": items,
        "operation": operation,
        "divisible_by_test": divisible_by_test,
        "throw": {
            True: if_true_throw,
            False: if_false_throw,
        },
        "items_inspected": 0,
    }


def parse_input(data):
    monkey_data = data.strip().split("\n\n")
    monkeys = map(lambda d: parse_monkey_data(d), monkey_data)
    return list(monkeys)


def main():
    with open("input/input_day11.txt") as f:
        data = f.read()
    # data = EXAMPLE_DATA
    data = parse_input(data)
    monkeys1 = copy.deepcopy(data)
    puzzle1(monkeys1)
    puzzle2(data)


if __name__ == "__main__":
    main()
