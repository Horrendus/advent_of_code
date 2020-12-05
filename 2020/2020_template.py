def puzzle1(data):
    pass


def puzzle2(data):
    pass


def parse_input(data):
    return data.split("\n")


def main():
    with open("input/input_day1.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
