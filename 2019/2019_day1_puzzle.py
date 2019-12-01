def puzzle1(data):
    sum_fuel = 0
    for line in data:
        sum_fuel = sum_fuel + int(int(line) / 3) - 2
    print("Puzzle 1:", sum_fuel)


def puzzle2(data):
    sum_fuel = 0
    for line in data:
        additional_fuel = int(line)
        while True:
            additional_fuel = int(additional_fuel / 3) - 2
            if additional_fuel >= 0:
                sum_fuel += additional_fuel
            else:
                break
    print("Puzzle 2:", sum_fuel)


def main():
    with open("input/input_day1.txt") as f:
        data = f.readlines()
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
