def most_common_bit(data, pos):
    count_0 = 0
    count_1 = 0
    half_data_len = int(len(data) / 2)
    for num in data:
        if num[pos] == "0":
            count_0 += 1
        elif num[pos] == "1":
            count_1 += 1
        if count_0 > half_data_len:
            return "0"
        if count_1 > half_data_len:
            return "1"
    return "1"


def puzzle1(data):
    most_common = []
    for i in range(len(data[0])):
        bit = most_common_bit(data, i)
        most_common.append(bit)

    gamma_rate = int("0b" + "".join(most_common), 2)
    epsilon_rate = int(
        "0b" + "".join(["1" if i == "0" else "0" for i in most_common]), 2
    )
    print(
        f"Puzzle 1: gamma rate {gamma_rate}, epsilon rate {epsilon_rate}, answer: {gamma_rate*epsilon_rate}"
    )


def puzzle2(data):
    o2_generator_rating_list = list(data)
    co2_scrubber_rating_list = list(data)
    print("Data: ", data)
    for i in range(len(data[0])):
        if len(o2_generator_rating_list) > 1:
            o2_bit = most_common_bit(o2_generator_rating_list, i)
            o2_generator_rating_list = [
                num for num in o2_generator_rating_list if num[i] == o2_bit
            ]
        if len(co2_scrubber_rating_list) > 1:
            co2_bit = most_common_bit(co2_scrubber_rating_list, i)
            co2_bit_flip = "1" if co2_bit == "0" else "0"
            co2_scrubber_rating_list = [
                num for num in co2_scrubber_rating_list if num[i] == co2_bit_flip
            ]
        if len(o2_generator_rating_list) == 1 and len(co2_scrubber_rating_list) == 1:
            break
    o2_generator_rating = int("0b" + "".join(o2_generator_rating_list[0]), 2)
    co2_scrubber_rating = int("0b" + "".join(co2_scrubber_rating_list[0]), 2)
    print(
        f"Puzzle 2: O2 generator rating: {o2_generator_rating}, CO2 scrubber rating: {co2_scrubber_rating}, answer: "
        f"{o2_generator_rating*co2_scrubber_rating}"
    )


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
