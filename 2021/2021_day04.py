import copy
from copy import deepcopy


def bingo_round(number, board):
    bingo = False
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == number:
                board[row][column] = None
                board_column = [board[i][column] for i in range(len(board))]
                board_row = board[row]
                if (board_row[0] is None and len(set(board_row)) == 1) or (
                    board_column[0] is None and len(set(board_column)) == 1
                ):
                    bingo = True
    return bingo


def play_bingo(numbers, boards):
    winning_board = None
    bingo = False
    for number in numbers:
        for board in boards:
            current_board_bingo = bingo_round(number, board)
            if current_board_bingo and not bingo:
                bingo = True
                winning_board = board
        if bingo:
            return True, number, winning_board
    return False, number, None


def calculate_board_sum_unmarked(board):
    sum = 0
    for row in board:
        for num in row:
            if num:
                sum += num
    return sum


def puzzle1(data):
    numbers, boards = data
    bingo, number, board = play_bingo(numbers, boards)
    if bingo:
        sum = calculate_board_sum_unmarked(board)
        print("Puzzle 1: ", sum * number)
    else:
        print("Puzzle 1: no board won, should not happen")


def puzzle2(data):
    numbers, boards = data
    last_winning_board = None
    last_winning_number = None
    for number in numbers:
        winning_boards = []
        for board in boards:
            bingo = bingo_round(number, board)
            if bingo:
                winning_boards.append(board)
                last_winning_board = board
                last_winning_number = number
        for board in winning_boards:
            boards.remove(board)
    sum = calculate_board_sum_unmarked(last_winning_board)
    print("Puzzle 1: ", sum * last_winning_number)


def parse_input(data):
    numbers_line = data.split("\n")[0]
    numbers = [int(n) for n in numbers_line.split(",")]
    board_lines = data.split("\n\n")[1:]
    boards = []
    for board_line in board_lines:
        board = []
        for line in board_line.split("\n"):
            if line.strip() != "":
                board_numbers = []
                board_numbers_splitted = line.split(" ")
                for number in board_numbers_splitted:
                    if number:
                        board_numbers.append(int(number))
                board.append(board_numbers)
        boards.append(board)
    return numbers, boards


def main():
    with open("input/input_day04.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(copy.deepcopy(data))
    puzzle2(data)


if __name__ == "__main__":
    main()
