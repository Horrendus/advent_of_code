from collections import defaultdict


def calculate_fish_school(data, total_days):
    fish_school = defaultdict(lambda: 0)
    for fish in data:
        fish_school[fish] += 1

    for i in range(total_days):
        fish_school_cycle = defaultdict(lambda: 0)

        for day in fish_school.keys():
            if day == 0:
                fish_school_cycle[8] += fish_school[0]
                fish_school_cycle[6] += fish_school[0]
            else:
                fish_school_cycle[day - 1] += fish_school[day]
        fish_school = fish_school_cycle

    return fish_school


def puzzle1(data):
    fish_school = calculate_fish_school(data, 80)
    print("Puzzle 1: ", sum(fish_school.values()))


def puzzle2(data):
    fish_school = calculate_fish_school(data, 256)
    print("Puzzle 2: ", sum(fish_school.values()))


def parse_input(data):
    return [int(n) for n in data.strip().split(",")]


def main():
    with open("input/input_day06.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
