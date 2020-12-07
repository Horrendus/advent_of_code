import re

from collections import defaultdict


def preprocess_line(line):
    line = line.rstrip(".")
    line = line.replace("bags", "")
    line = line.replace("bag", "")
    # line = re.sub(r'[0-9]+', '', line)
    return line


def parse_container_data(data):
    contains = defaultdict(list)
    contained_in = defaultdict(list)
    for line in data:
        line = preprocess_line(line)
        container, _, contained_bags = line.partition("  contain ")
        container = container.strip()
        if contained_bags != "no other ":
            contained_bags = contained_bags.split(",")
            for contained_bag in contained_bags:
                contained_bag = contained_bag.strip()
                pos = contained_bag.find(" ")
                contained_amount = int(contained_bag[:pos])
                bag_color = contained_bag[pos:].strip()
                contained_in[bag_color].append(container)
                contains[container].append((contained_amount, bag_color))

    return contains, contained_in


def puzzle1(container_data):
    contained_in = container_data[1]
    color_queue = ["shiny gold"]
    colors = []
    while True:
        color = color_queue.pop()
        if color in contained_in:
            colors.extend(contained_in[color])
            color_queue.extend(contained_in[color])
        if len(color_queue) == 0:
            break
    print("Puzzle 1: ", len(set(colors)))


def count_contains(contains, bag):
    if len(contains[bag]) == 0:
        return 1
    else:
        sum = 1
        for contained_bag in contains[bag]:
            sum += contained_bag[0] * count_contains(contains, contained_bag[1])
        return sum


def puzzle2(container_data):
    contains = container_data[0]
    count = count_contains(contains, "shiny gold")
    print("Puzzle 2: ", count - 1)  # off by one, dont wanna fix :)


def parse_input(data):
    return data.split("\n")


def main():
    with open("input/input_day7.txt") as f:
        data = f.read()
    data = parse_input(data)
    container_data = parse_container_data(data)
    puzzle1(container_data)
    puzzle2(container_data)


if __name__ == "__main__":
    main()
