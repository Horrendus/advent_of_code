import re

NUM_MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def puzzle1(data):
    calibration_value = 0
    for s in data:
        for c in s:
            if c.isdigit():
                calibration_value += int(c) * 10
                break
        for c in reversed(s):
            if c.isdigit():
                calibration_value += int(c)
                break
    print("Puzzle 1: ", calibration_value)


def puzzle2(data):
    nums_regex = r"|".join([num for num in NUM_MAP])
    nums_regex += r"|\d"

    nums_regex_rev = r"|".join([num[::-1] for num in NUM_MAP])
    nums_regex_rev += r"|\d"
    calibration_value = 0
    for s in data:
        m = re.search(nums_regex, s)
        if not m[0].isdigit():
            first_digit = NUM_MAP[m[0]]
        else:
            first_digit = int(m[0])

        m2 = re.search(nums_regex_rev, s[::-1])
        if not m2[0].isdigit():
            second_digit = NUM_MAP[m2[0][::-1]]
        else:
            second_digit = int(m2[0])
        calibration_value += first_digit * 10
        calibration_value += second_digit

    print("Puzzle 2: ", calibration_value)


def parse_input(data):
    return data.strip().split("\n")


def main():
    with open("input/input_day01.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
