def calculate_priority(letter):
    if letter.isupper():
        return ord(letter) - ord("A") + 27
    return ord(letter) - ord("a") + 1


def puzzle1(data):
    data = [(line[: int(len(line) / 2)], line[int(len(line) / 2) :]) for line in data]
    shared_items = [list(set(line[0]).intersection(line[1]))[0] for line in data]
    priorities = sum(map(lambda letter: calculate_priority(letter), shared_items))
    print("Puzzle 1: ", priorities)


def puzzle2(data):
    priorities = 0
    for i in range(0, len(data), 3):
        shared_items = list(
            set(data[i]).intersection(data[i + 1]).intersection(data[i + 2])
        )
        priorities += calculate_priority(shared_items[0])
    print("Puzzle 2: ", priorities)


def parse_input(data):
    return data.strip().split("\n")


def main():
    with open("input/input_day03.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
