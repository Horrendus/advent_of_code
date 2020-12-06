from collections import defaultdict


def puzzle1(data):
    group_answer_count = []
    for group in data:
        group_answers = []
        for answer in group.split("\n"):
            for q in answer:
                group_answers.append(q)
        group_answer_count.append(len(set(group_answers)))
    print("Puzzle 1: ", sum(group_answer_count))


def puzzle2(data):
    group_answer_count = []
    for group in data:
        individual_answers = group.split("\n")
        group_answers = defaultdict(int)
        for answer in individual_answers:
            for q in answer:
                group_answers[q] = group_answers[q] + 1
        group_count = 0
        for q in group_answers:
            if group_answers[q] == len(individual_answers):
                group_count += 1
        group_answer_count.append(group_count)
    print("Puzzle 2: ", sum(group_answer_count))


def parse_input(data):
    return data.split("\n\n")


def main():
    with open("input/input_day6.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
