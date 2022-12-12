from collections import defaultdict

from queue import PriorityQueue


# Graph class & Dijkstra algorithm adapted from
# https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/dijkstras-algorithm/
class Graph:
    def __init__(self, size_x, size_y):
        self.v = size_x * size_y
        self.edges = defaultdict(list)

    def add_edge(self, u, v):
        self.edges[u].append(v)


def dijkstra(graph, start_vertex):
    D = defaultdict(lambda: float("inf"))
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))
    visited = []

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.append(current_vertex)

        for neighbor in graph.edges[current_vertex]:
            distance = 1
            if neighbor not in visited:
                old_cost = D[neighbor]
                new_cost = D[current_vertex] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, neighbor))
                    D[neighbor] = new_cost
    return D


def get_neighbor_coordinates(
    pos: tuple[int, int], matrix_size_y, matrix_size_x
) -> list[tuple[int, int]]:
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


def puzzle1(data):
    d = dijkstra(data[0], data[1])
    print("Puzzle 1:", d[data[2]])


def puzzle2(data):
    steps = []
    for start_node in data[3]:
        d = dijkstra(data[0], start_node)
        if d[data[2]] != float("inf"):
            steps.append(d[data[2]])
    print("Puzzle 2:", sorted(steps)[0])


def get_elevation_level(elevation_char):
    if elevation_char == "S":
        elevation_char = "a"
    if elevation_char == "E":
        elevation_char = "z"
    elevation_level = ord(elevation_char) - ord("a")
    return elevation_level


def parse_input(data):
    lines = data.strip().split("\n")
    size_x = len(lines[0])
    size_y = len(lines)
    g = Graph(size_x, size_y)
    start_node = None
    end_node = None
    a_nodes = []
    for y in range(size_y):
        for x in range(size_x):
            current = lines[y][x]
            current_elevation = get_elevation_level(current)
            neighbors = get_neighbor_coordinates((y, x), size_y, size_x)
            if current == "E":
                end_node = (y, x)
            if current == "S":
                start_node = (y, x)
            if current == "a":
                a_nodes.append((y, x))
            for neighbor in neighbors:
                if (
                    get_elevation_level(lines[neighbor[0]][neighbor[1]])
                    <= current_elevation + 1
                ):
                    g.add_edge((y, x), neighbor)
    return (g, start_node, end_node, a_nodes)


def main():
    with open("input/input_day12.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
