EXAMPLE_DATA = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""


def make_grid(cubes):
    max_x = cubes[-1][0] + 1
    max_y = cubes[-1][1] + 1
    max_z = cubes[-1][2] + 1
    max_grid = max(max_x, max_y, max_z)
    grid = [
        [[0 for _ in range(max_grid + 2)] for _ in range(max_grid + 2)]
        for _ in range(max_grid + 2)
    ]
    for cube in cubes:
        grid[cube[0]][cube[1]][cube[2]] = 1

    return grid, max_grid


def count_neighbours(cube_pos, grid):
    x, y, z = cube_pos
    neighbours = [
        grid[x][y][z + 1],
        grid[x][y][z - 1],
        grid[x][y + 1][z],
        grid[x][y - 1][z],
        grid[x + 1][y][z],
        grid[x - 1][y][z],
    ]
    return sum(neighbours)


def puzzle1(cubes):
    grid, max_grid = make_grid(cubes)

    surface_area = 0
    for x in range(max_grid + 1):
        for y in range(max_grid + 1):
            for z in range(max_grid + 1):
                if grid[x][y][z]:
                    surface_area += 6 - count_neighbours((x, y, z), grid)
    print("Puzzle 1: ", surface_area)


def puzzle2(data):
    pass


def parse_input(data):
    lines = data.strip().split("\n")
    splitted_lines = map(lambda line: line.split(","), lines)
    cubes = [(int(cube[0]), int(cube[1]), int(cube[2])) for cube in splitted_lines]
    sorted_cubes = sorted(cubes)
    return sorted_cubes


def main():
    with open("input/input_day18.txt") as f:
        data = f.read()
    # data = EXAMPLE_DATA
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
