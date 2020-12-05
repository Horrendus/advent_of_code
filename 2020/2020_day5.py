def decode_row(row):
    bin_row = row.replace("F", "0").replace("B", "1")
    return int(bin_row, 2)


def decode_column(column):
    bin_column = column.replace("L", "0").replace("R", "1")
    return int(bin_column, 2)


def get_all_seat_ids(data):
    seat_ids = []
    for line in data:
        row = decode_row(line[:7])
        column = decode_column(line[7:])
        seat_id = row * 8 + column
        seat_ids.append(seat_id)
    return seat_ids


def puzzle1(data):
    print("Max Seat ID: ", max(get_all_seat_ids(data)))


def puzzle2(data):
    seat_ids = get_all_seat_ids(data)
    seat_ids.sort()
    missing = 0
    for i in range(1, seat_ids[-2]):
        if seat_ids[i] - seat_ids[i-1] != 1:
            missing = seat_ids[i-1] + 1
            break
        elif seat_ids[i+1] - seat_ids[i] != 1:
            missing = seat_ids[i+1] - 1
            break
    print("Missing SeatID: ", missing)



def parse_input(data):
    return data.split("\n")


def main():
    with open("input/input_day5.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
