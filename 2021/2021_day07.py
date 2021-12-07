import statistics
import sys


def puzzle1(data):
    m = int(statistics.mean(data))
    minimum_fuel = sum([abs(x - m) for x in data])
    n = m
    while True:
        n = n + 1
        fuel = sum([abs(x - n) for x in data])
        if fuel < minimum_fuel:
            minimum_fuel = fuel
        else:
            break
    n = m
    while True:
        n = n - 1
        fuel = sum([abs(x - n) for x in data])
        if fuel < minimum_fuel:
            minimum_fuel = fuel
        else:
            break

    print("Puzzle 1: ", minimum_fuel)


def puzzle2(data):
    m = int(statistics.mean(data))
    minimum_fuel = sum([sum(range(1, abs(x - m) + 1)) for x in data])
    n = m
    while True:
        n = n + 1
        fuel = sum([sum(range(1, abs(x - n) + 1)) for x in data])
        if fuel < minimum_fuel:
            minimum_fuel = fuel
        else:
            break
    n = m
    while True:
        n = n - 1
        fuel = sum([sum(range(1, abs(x - n) + 1)) for x in data])
        if fuel < minimum_fuel:
            minimum_fuel = fuel
        else:
            break

    print("Puzzle 2: ", minimum_fuel)


def parse_input(data):
    return [int(d) for d in data.split(",")]


def main():
    with open("input/input_day07.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
