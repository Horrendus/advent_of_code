deterministic_dice_rolls = 0


def roll_deterministic_dice():
    global deterministic_dice_rolls
    dice_value = (deterministic_dice_rolls % 100) + 1
    deterministic_dice_rolls += 1
    return dice_value


def puzzle1(data):
    track = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    players = [{"score": 0, "pos": data[0]}, {"score": 0, "pos": data[1]}]
    current_player = 0
    while True:
        player = players[current_player]
        dice_value = (
            roll_deterministic_dice()
            + roll_deterministic_dice()
            + roll_deterministic_dice()
        )
        player["pos"] = track[(player["pos"] + dice_value) % 10]
        player["score"] += player["pos"]
        if player["score"] >= 1000:
            break
        current_player = (current_player + 1) % len(players)
    loser = min(players, key=lambda p: p["score"])
    print("Puzzle 1: ", loser["score"] * deterministic_dice_rolls)


def puzzle2(data):
    pass


def parse_input(data):
    return data.strip().split("\n")


def main():
    data = (3, 7)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
