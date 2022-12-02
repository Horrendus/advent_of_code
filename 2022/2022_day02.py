SHAPE_SCORE = {"A": 1, "B": 2, "C": 3}


def score_round(your_choice, opponent_choice) -> int:
    score = SHAPE_SCORE[your_choice]
    if your_choice == opponent_choice:
        return score + 3  # DRAW
    if (
        your_choice == "A"
        and opponent_choice == "C"
        or your_choice == "B"
        and opponent_choice == "A"
        or your_choice == "C"
        and opponent_choice == "B"
    ):
        return score + 6  # WIN
    return score  # LOSS


def choose_shape(opponent_choice, outcome):
    if outcome == "Y":
        # DRAW
        return opponent_choice
    if outcome == "Z":
        # WIN
        if opponent_choice == "A":
            return "B"
        if opponent_choice == "B":
            return "C"
        if opponent_choice == "C":
            return "A"
    if outcome == "X":
        # LOOSE
        if opponent_choice == "A":
            return "C"
        if opponent_choice == "B":
            return "A"
        if opponent_choice == "C":
            return "B"


def score_strategy(strategy):
    score = sum(map(lambda round: score_round(round[1], round[0]), strategy))
    return score


def puzzle1(data):
    strategy = list(map(lambda round: [round[0], chr(ord(round[1]) - 23)], data))
    score = score_strategy(strategy)
    print("Puzzle 1: ", score)


def puzzle2(data):
    strategy = list(
        map(lambda round: [round[0], choose_shape(round[0], round[1])], data)
    )
    score = score_strategy(strategy)
    print("Puzzle 2: ", score)


def parse_input(data):
    return list(map(lambda line: line.split(" "), data.strip().split("\n")))


def main():
    with open("input/input_day02.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
