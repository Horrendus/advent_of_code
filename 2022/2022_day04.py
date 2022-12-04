import re


def fully_includes(range1, range2):
    return (
        int(range2[0]) >= int(range1[0])
        and int(range2[0]) <= int(range1[1])
        and int(range2[1]) >= int(range1[0])
        and int(range2[1]) <= int(range1[1])
    )


def overlaps(range1, range2):
    return (int(range2[0]) >= int(range1[0]) and int(range2[0]) <= int(range1[1])) or (
        int(range2[1]) >= int(range1[0]) and int(range2[1]) <= int(range1[1])
    )


def puzzle1(data):
    count = sum(
        [
            fully_includes((r[0], r[1]), (r[2], r[3]))
            or fully_includes((r[2], r[3]), (r[0], r[1]))
            for r in data
        ]
    )
    print("Puzzle 1: ", count)


def puzzle2(data):
    count = sum(
        [
            overlaps((r[0], r[1]), (r[2], r[3])) or overlaps((r[2], r[3]), (r[0], r[1]))
            for r in data
        ]
    )
    print("Puzzle 1: ", count)


def parse_input(data):
    return list(map(lambda line: re.split("[-,]", line), data.strip().split("\n")))


def main():
    with open("input/input_day04.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
