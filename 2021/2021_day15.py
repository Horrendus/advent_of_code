from queue import PriorityQueue

from typing import List, Tuple


def get_neighbor_coordinates(
    pos: Tuple[int, int], matrix_size_x, matrix_size_y
) -> List[Tuple[int, int]]:
    y, x = pos
    neighbor_list = []
    # left: (y, x-1), down: (y+1, x), right: (y, x+1), up: (y-1, x)
    if x > 0:
        neighbor_list.append((y, x - 1))
    if y < matrix_size_y - 1:
        neighbor_list.append((y + 1, x))
    if x < matrix_size_x - 1:
        neighbor_list.append((y, x + 1))
    if y > 0:
        neighbor_list.append((y - 1, x))
    return neighbor_list


# Dijkstra algorithm adapted from https://stackabuse.com/dijkstras-algorithm-in-python/
def dijkstra(graph, start_vertex, matrix_size_x, matrix_size_y):
    d = {
        (i, j): float("inf") for i in range(matrix_size_x) for j in range(matrix_size_y)
    }
    d[start_vertex] = 0
    visited = {
        (i, j): False for i in range(matrix_size_x) for j in range(matrix_size_y)
    }

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited[current_vertex] = True

        for neighbor in get_neighbor_coordinates(
            current_vertex, matrix_size_x, matrix_size_y
        ):
            distance = graph[neighbor[0]][neighbor[1]]
            if not visited[neighbor]:
                old_cost = d[neighbor]
                new_cost = d[current_vertex] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, neighbor))
                    d[neighbor] = new_cost
    return d


def extend_map(data):
    numbers = [9, 1, 2, 3, 4, 5, 6, 7, 8]
    extended_map = []
    for i in range(5):
        for row in data:
            row_input = list(map(lambda x: numbers[(x + i) % 9], row))
            extended_row = []
            for j in range(5):
                extended_row.extend(
                    list(map(lambda x: numbers[(x + j) % 9], row_input))
                )
            extended_map.append(extended_row)

    return extended_map


def puzzle1(data):
    d = dijkstra(data, (0, 0), len(data), len(data))
    print("Puzzle 1: ", d[(len(data) - 1, len(data) - 1)])


def puzzle2(data):
    extended_map = extend_map(data)
    d = dijkstra(extended_map, (0, 0), len(extended_map), len(extended_map))
    print("Puzzle 2: ", d[(len(extended_map) - 1, len(extended_map) - 1)])


def parse_input(data):
    lines = data.strip().split("\n")
    matrix = []
    for line in lines:
        row = list(map(int, line))
        matrix.append(row)
    return matrix


def main():
    with open("input/input_day15.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
