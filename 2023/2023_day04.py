def puzzle1(cards):
    card_values = 0
    for card in cards.values():
        card_value = 0
        for winning_number in card["winning_numbers"]:
            if winning_number in card["numbers"]:
                if card_value == 0:
                    card_value = 1
                else:
                    card_value *= 2
        card_values += card_value
    print("Puzzle 1: ", card_values)


def puzzle2(cards):
    for card_id in cards:
        card = cards[card_id]
        match_count = 0
        for winning_number in card["winning_numbers"]:
            if winning_number in card["numbers"]:
                match_count += 1
        next_card_id = card_id + 1
        for id in range(next_card_id, next_card_id + match_count):
            cards[id]["copies"] += card["copies"]
    print("Puzzle 2: ", sum([card["copies"] for card in cards.values()]))


def parse_input(data):
    lines = data.strip().split("\n")
    cards = dict()
    for line in lines:
        card_id_str, card_data = line[4:].split(":")
        card_id = int(card_id_str.strip())
        winning_numbers_str, numbers_str = card_data.split("|")
        winning_numbers = [
            int(number) for number in winning_numbers_str.strip().split(" ") if number
        ]
        numbers = [int(number) for number in numbers_str.strip().split(" ") if number]
        cards[card_id] = {
            "numbers": numbers,
            "winning_numbers": winning_numbers,
            "copies": 1,
        }
    return cards


def main():
    with open("input/input_day04.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
