from typing import List


def is_sum_of_two_elements(number: int, arr: List[int]):
    for i in range(len(arr) - 1):
        first = arr[i]
        for j in range(i, len(arr)):
            second = arr[j]
            if first + second == number and i != j:
                return True
    return False


def puzzle1(data):
    for i in range(25, len(data)):
        arr = data[i-25:i]
        if not is_sum_of_two_elements(data[i], arr):
            print("Puzzle 1: ", data[i])
            return data[i]
    print("Puzzle 1: this shouldnt happen")


def puzzle2(data, number):
    data = data.sort()


def parse_input(data):
    return list(map(int, data.split("\n")))


def main():
    with open("input/input_day9.txt") as f:
        data = f.read()
    data = parse_input(data)
    number = puzzle1(data)
    puzzle2(data, number)


if __name__ == "__main__":
    main()
