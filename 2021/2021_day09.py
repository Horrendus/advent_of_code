from typing import List, Tuple

MATRIX_SIZE_X = 100
MATRIX_SIZE_Y = 100


def get_neighbor_coordinates(pos: Tuple[int, int]) -> List[Tuple[int, int]]:
    y, x = pos
    neighbor_list = []
    # left: (y, x-1), down: (y+1, x), right: (y, x+1), up: (y-1, x)
    if x > 0:
        neighbor_list.append((y, x - 1))
    if y < MATRIX_SIZE_Y - 1:
        neighbor_list.append((y + 1, x))
    if x < MATRIX_SIZE_X - 1:
        neighbor_list.append((y, x + 1))
    if y > 0:
        neighbor_list.append((y - 1, x))
    return neighbor_list


def get_neighbors(pos: Tuple[int, int], matrix: List[List[int]]) -> List[int]:
    neigbor_list = get_neighbor_coordinates(pos)
    neighbor_values = []
    for neighbor in neigbor_list:
        neighbor_values.append(matrix[neighbor[0]][neighbor[1]])
    return neighbor_values


def get_low_points(matrix: List[List[int]]) -> List[Tuple[int, int]]:
    low_points = []
    for y in range(MATRIX_SIZE_Y):
        for x in range(MATRIX_SIZE_X):
            neighbors = get_neighbors((y, x), matrix)
            if matrix[y][x] < min(neighbors):
                low_points.append((y, x))
    return low_points


def puzzle1(matrix):
    low_points_value = [matrix[p[0]][p[1]] + 1 for p in get_low_points(matrix)]
    print("Puzzle 1: ", sum(low_points_value))


def find_region_around_point(pos: Tuple[int, int], matrix: List[List[int]]) -> int:
    points = [pos]
    region = [pos]
    while len(points) > 0:
        pos = points.pop()
        neighbors = get_neighbor_coordinates(pos)
        for neighbor in neighbors:
            if neighbor not in region and matrix[neighbor[0]][neighbor[1]] != 9:
                region.append(neighbor)
                points.append(neighbor)

    return len(region)


def puzzle2(matrix):
    low_points = get_low_points(matrix)
    regions = []
    for low_point in low_points:
        regions.append(find_region_around_point(low_point, matrix))
    regions.sort()
    biggest_regions = regions[len(regions) - 3 :]
    print("Puzzle 2: ", biggest_regions[0] * biggest_regions[1] * biggest_regions[2])


def parse_input(data):
    lines = data.strip().split("\n")
    return [[int(num) for num in line] for line in lines]


def main():
    with open("input/input_day09.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
