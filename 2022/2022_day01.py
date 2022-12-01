import functools


def puzzle1(data):
    calories_per_elf = map(lambda calories: sum(calories), data)
    print("Puzzle 1: ", max(calories_per_elf))


def puzzle2(data):
    calories_per_elf = sorted(map(lambda calories: sum(calories), data), reverse=True)
    print("Puzzle 2: ", sum(calories_per_elf[:3]))


def parse_input(data):
    l = list(map(lambda line: line.split("\n"), data.strip().split("\n\n")))
    return list(
        map(
            lambda calorie_list: list(map(lambda calorie: int(calorie), calorie_list)),
            l,
        )
    )


def main():
    with open("input/input_day01.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
