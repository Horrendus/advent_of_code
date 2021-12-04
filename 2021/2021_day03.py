def puzzle1(data):
    most_common = []
    half_data_len = int(len(data) / 2)
    for i in range(len(data[0])):
        count_0 = 0
        count_1 = 0
        for l in data:
            if l[i] == "0":
                count_0 += 1
            elif l[i] == "1":
                count_1 += 1
            if count_0 > half_data_len:
                most_common.append("0")
                break
            if count_1 > half_data_len:
                most_common.append("1")
                break

    gamma_rate = int("0b" + "".join(most_common), 2)
    epsilon_rate = int(
        "0b" + "".join(["1" if i == "0" else "0" for i in most_common]), 2
    )
    print(
        f"Puzzle 1: gamma rate {gamma_rate}, epsilon rate {epsilon_rate}, answer: {gamma_rate*epsilon_rate}"
    )


def puzzle2(data):
    pass


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
