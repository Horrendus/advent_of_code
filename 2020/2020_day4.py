import re


def process_line(line):
    line_dict = dict()
    key_value_pairs = line.split(" ")
    for key_value_pair in key_value_pairs:
        splitted = key_value_pair.split(":")
        line_dict[splitted[0]] = splitted[1]
    return line_dict


def parse_passports(data):
    passports = []
    passport_data = dict()
    for line in data:
        if not line:
            passports.append(passport_data)
            passport_data = dict()
        else:
            passport_data.update(process_line(line))
    return passports


def validate_height(height):
    try:
        if len(height) >= 4 and len(height) <= 5:
            unit = height[-2:]
            value = int(height[:-2])
            if unit == "in":
                return value in range(59, 77)
            elif unit == "cm":
                return value in range(150, 194)
    except ValueError:
        pass
    return False


def puzzle1(data):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_passports = 0
    passports = parse_passports(data)
    for passport in passports:
        if (all([(req_key in passport.keys()) for req_key in required_fields])):
            valid_passports += 1

    print("Puzzle 1: ", valid_passports)


def puzzle2(data):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    hcl_pattern = re.compile("#([a-f]|[0-9]){6}$")
    pid_pattern = re.compile("^[0-9]{9}$")
    valid_passports = 0
    passports = parse_passports(data)
    for passport in passports:
        if (all([(req_key in passport.keys()) for req_key in required_fields])):
            passport_validation = []
            passport_validation.append(int(passport["byr"]) in range(1920, 2003))
            passport_validation.append(int(passport["iyr"]) in range(2010, 2021))
            passport_validation.append(int(passport["eyr"]) in range(2020, 2031))
            passport_validation.append(validate_height(passport["hgt"]))
            passport_validation.append(hcl_pattern.match(passport["hcl"]) is not None)
            passport_validation.append(passport["ecl"] in valid_eye_colors)
            passport_validation.append(pid_pattern.match(passport["pid"]) is not None)
            if passport_validation and all(passport_validation):
                valid_passports += 1

    print("Puzzle 2: ", valid_passports)


def parse_input(data):
    return data.split("\n")


def main():
    with open("input/input_day4.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
