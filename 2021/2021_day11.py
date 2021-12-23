import copy

from typing import Tuple, List

MATRIX_SIZE_X = 10
MATRIX_SIZE_Y = 10


def get_neighbor_coordinates(pos: Tuple[int, int]) -> List[Tuple[int, int]]:
    y, x = pos
    neighbor_list = []
    # left: (y, x-1), down: (y+1, x), right: (y, x+1), up: (y-1, x)
    # up-left: (y-1, x-1), down-left: (y+1, x-1), up-right: (y-1, x+1), down-right: (y+1, x+1)
    if x > 0:
        neighbor_list.append((y, x - 1))
    if y < MATRIX_SIZE_Y - 1:
        neighbor_list.append((y + 1, x))
    if x < MATRIX_SIZE_X - 1:
        neighbor_list.append((y, x + 1))
    if y > 0:
        neighbor_list.append((y - 1, x))
    if y > 0 and x > 0:
        neighbor_list.append((y - 1, x - 1))
    if y < MATRIX_SIZE_Y - 1 and x > 0:
        neighbor_list.append((y + 1, x - 1))
    if y > 0 and x < MATRIX_SIZE_X - 1:
        neighbor_list.append((y - 1, x + 1))
    if y < MATRIX_SIZE_Y - 1 and x < MATRIX_SIZE_X - 1:
        neighbor_list.append((y + 1, x + 1))
    return neighbor_list


def puzzle1(data):
    flashers = []
    flash_count = 0

    for step in range(100):
        for y in range(MATRIX_SIZE_Y):
            for x in range(MATRIX_SIZE_X):
                data[y][x] += 1
                if data[y][x] > 9:
                    flashers.append((y, x))

        while len(flashers) > 0:
            flasher = flashers.pop()
            flasher_y, flasher_x = flasher
            flash_count += 1
            data[flasher_y][flasher_x] = 0
            neighbors = get_neighbor_coordinates(flasher)
            for neighbor in neighbors:
                neighbor_y, neighbor_x = neighbor
                # only add energy to neighbors if they aren't 0 (flashed already during this turn)
                if data[neighbor_y][neighbor_x] != 0:
                    data[neighbor_y][neighbor_x] += 1
                    if data[neighbor_y][neighbor_x] > 9 and neighbor not in flashers:
                        flashers.append(neighbor)

    print("Puzzle 1: ", flash_count)


def puzzle2(data):
    flashers = []
    turn_flash_count = 0
    step = 0

    while turn_flash_count != (MATRIX_SIZE_X * MATRIX_SIZE_Y):
        step += 1
        turn_flash_count = 0
        for y in range(MATRIX_SIZE_Y):
            for x in range(MATRIX_SIZE_X):
                data[y][x] += 1
                if data[y][x] > 9:
                    flashers.append((y, x))

        while len(flashers) > 0:
            flasher = flashers.pop()
            flasher_y, flasher_x = flasher
            data[flasher_y][flasher_x] = 0
            turn_flash_count += 1
            neighbors = get_neighbor_coordinates(flasher)
            for neighbor in neighbors:
                neighbor_y, neighbor_x = neighbor
                # only add energy to neighbors if they aren't 0 (flashed already during this turn)
                if data[neighbor_y][neighbor_x] != 0:
                    data[neighbor_y][neighbor_x] += 1
                    if data[neighbor_y][neighbor_x] > 9 and neighbor not in flashers:
                        flashers.append(neighbor)

    print("Puzzle 2: ", step)


def parse_input(data):
    lines = data.strip().split("\n")
    matrix = [list(map(int, line)) for line in lines]
    return matrix


def main():
    with open("input/input_day11.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(copy.deepcopy(data))
    puzzle2(data)


if __name__ == "__main__":
    main()
