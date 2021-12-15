from collections import Counter


def puzzle1(data):
    steps = 10
    polymer = data[0]
    rules = data[1]
    for i in range(steps):
        polymer_extension = ""
        for i in range(0, len(polymer) - 1):
            pair = polymer[i : i + 2]
            polymer_extension += rules[pair]

        extended_polymer = ""
        for i in range(len(polymer)):
            extended_polymer += polymer[i]
            if i < len(polymer_extension):
                extended_polymer += polymer_extension[i]

        polymer = extended_polymer

    counter = Counter(polymer)
    least_common = min(counter.values())
    most_common = max(counter.values())
    answer = most_common - least_common
    print("Puzzle 1: ", answer)


def puzzle2(data):
    pass


def parse_input(data):
    lines = data.strip().split("\n")
    polymer_template = lines[0]
    rules = dict()
    for line in lines[2:]:
        rule_in, rule_out = line.split(" -> ")
        rules[rule_in] = rule_out
    return (polymer_template, rules)


def main():
    with open("input/input_day14.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
