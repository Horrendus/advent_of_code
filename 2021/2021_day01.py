def puzzle1(data):
    last = data[0]
    increases = 0
    for num in data:
        if num > last:
            increases += 1
        last = num
    print("Puzzle 1: ", increases)


def puzzle2(data):
    last_sum = data[0] + data[1] + data[2]
    increases = 0
    for i in range(len(data)-2):
        sum = data[i] + data[i+1] + data[i+2]
        if sum > last_sum:
            increases += 1
        last_sum = sum
    print("Puzzle 2: ", increases)


def parse_input(data):
    return [int(line) for line in data.strip().split("\n")]


def main():
    with open("input/input_day01.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
