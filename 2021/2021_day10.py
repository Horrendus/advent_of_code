import statistics

# map closing brackets to opening brackets
BRACKETS_MAP_CLOSE_TO_OPEN = {")": "(", "]": "[", "}": "{", ">": "<"}
BRACKETS_MAP_OPEN_TO_CLOSE = {"(": ")", "[": "]", "{": "}", "<": ">"}

POINTS_MAPPING_SYNTAX = {")": 3, "]": 57, "}": 1197, ">": 25137}
POINTS_MAPPING_AUTOCOMPLETE = {")": 1, "]": 2, "}": 3, ">": 4}


def syntax_check_line(line):
    match_stack = []
    for bracket in line:
        if bracket in BRACKETS_MAP_CLOSE_TO_OPEN:
            # closing bracket
            if (
                len(match_stack) == 0
                or match_stack[-1] != BRACKETS_MAP_CLOSE_TO_OPEN[bracket]
            ):
                return bracket, match_stack
            else:
                # matching bracket
                match_stack.pop()
        else:
            match_stack.append(bracket)
    return None, match_stack


def puzzle1(data):
    score = 0
    for line in data:
        check_result = syntax_check_line(line)
        if check_result[0]:
            score += POINTS_MAPPING_SYNTAX[check_result[0]]
    print("Puzzle 1: ", score)


def puzzle2(data):
    scores = []
    for line in data:
        check_result = syntax_check_line(line)
        if not check_result[0]:
            score = 0
            match_stack = check_result[1]
            while len(match_stack) > 0:
                bracket = match_stack.pop()
                match = BRACKETS_MAP_OPEN_TO_CLOSE[bracket]
                score = score * 5 + POINTS_MAPPING_AUTOCOMPLETE[match]
            scores.append(score)
        else:
            pass
            # print("Syntax Error: ", line)
    print("Puzzle 2: ", statistics.median(scores))


def parse_input(data):
    return data.strip().split("\n")


def main():
    with open("input/input_day10.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
