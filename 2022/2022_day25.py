def snafu_to_decimal(snafu_number: str) -> int:
    snafu_number = snafu_number[::-1]  #
    number = 0
    for i in range(len(snafu_number)):
        digit = snafu_number[i]
        if digit.isdigit():
            digit_dec = int(digit)
        elif digit == "=":
            digit_dec = -2
        else:  # digit == "-"
            digit_dec = -1
        number += digit_dec * 5 ** i
    return number


def decimal_to_snafu(number: int) -> str:
    snafu_digits = []
    carry = 0
    while number > 0 or carry == 1:
        number, remainder = divmod(number, 5)
        remainder += carry
        if remainder <= 2:
            snafu_digits.append(str(remainder))
            carry = 0
        else:
            if remainder == 3:
                snafu_digits.append("=")
            elif remainder == 4:
                snafu_digits.append("-")
            elif remainder == 5:
                snafu_digits.append(str(0))
            carry = 1
    return "".join(snafu_digits[::-1])


def puzzle1(data):
    decimal_sum = sum([snafu_to_decimal(snafu_number) for snafu_number in data])
    snafu_sum = decimal_to_snafu(decimal_sum)
    print("Puzzle 1:", snafu_sum)


def puzzle2(data):
    pass


def parse_input(data):
    return data.strip().split("\n")


def main():
    with open("input/input_day25.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
