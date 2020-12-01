GOAL = 2020


def puzzle1(data):
    for i in range(len(data)-1):
        first = data[i]
        for j in range(i, len(data)):
            second = data[j]
            if first + second == GOAL:
                print("first:  ", first)
                print("second: ", second)
                print("f*s:    ", first*second)
                # return


def puzzle2(data):
    for i in range(len(data) - 1):
        first = data[i]
        for j in range(i, len(data)):
            second = data[j]
            for k in range(len(data)):
                third = data[k]
                if first + second + third == GOAL:
                    print("first:  ", first)
                    print("second: ", second)
                    print("third:  ", second)
                    print("f*s*t:  ", first * second * third)
                    # return


def parse_input(data):
    return list(map(int, data.split("\n")))


def main():
    with open("input/input_day1.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
