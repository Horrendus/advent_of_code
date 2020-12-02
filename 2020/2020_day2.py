def puzzle1(data):
    valid_passwords = 0
    for password_info in data:
        count = password_info["password"].count(password_info["character"])
        if count >= password_info["lower"] and count <= password_info["upper"]:
            valid_passwords += 1

    print(valid_passwords)


def puzzle2(data):
    valid_passwords = 0
    for password_info in data:
        password, character, lower, upper = password_info["password"], password_info["character"], password_info["lower"], password_info["upper"]
        if (password[lower-1] == character) != (password[upper-1] == character):
            valid_passwords += 1

    print(valid_passwords)


def parse_input(data):
    parsed = []
    for line in data:
        splitted = line.split(":")
        password = splitted[1].strip()
        policy = splitted[0].split(" ")
        counts = policy[0].split("-")
        character = policy[1]

        parsed_line = {"lower": int(counts[0]), "upper": int(counts[1]), "character": character, "password": password}
        parsed.append(parsed_line)

    return parsed


def main():
    with open("input/input_day2.txt") as f:
        data = f.readlines()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
