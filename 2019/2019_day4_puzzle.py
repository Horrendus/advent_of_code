def check_password_1(number):
    has_double = False
    for i in range(len(number) - 1):
        if number[i] == number[i + 1]:
            has_double = True
        if number[i + 1] < number[i]:
            return False
    if has_double:
        return True
    return False


def check_password_2(number):
    number_occurences = dict()
    i = 0
    for i in range(len(number) - 1):
        if number[i + 1] < number[i]:
            return False
    for digit in set(number):
        number_occurences[digit] = number.count(digit)
    if 2 in number_occurences.values():
        return True
    return False


def puzzle1(first, second):
    checks = [check_password_1(str(number)) for number in range(first, second + 1)]
    print("Puzzle 1: ", sum(checks))


def puzzle2(first, second):
    checks = [check_password_2(str(number)) for number in range(first, second + 1)]
    print("Puzzle 2: ", sum(checks))


def main():
    data = input()
    numbers = data.split("-")
    first = int(numbers[0])
    second = int(numbers[1])
    puzzle1(first, second)
    puzzle2(first, second)


if __name__ == "__main__":
    main()
