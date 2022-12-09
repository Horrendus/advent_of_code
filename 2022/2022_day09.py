class Rope:
    def __init__(self, number_of_knots: int):
        self.knots = [(0, 0) for _ in range(number_of_knots)]
        self.tail_positions = set([])

    def move_head(self, direction: str):
        if direction == "U":
            self.knots[0] = (self.knots[0][0], self.knots[0][1] + 1)
        elif direction == "D":
            self.knots[0] = (self.knots[0][0], self.knots[0][1] - 1)
        elif direction == "R":
            self.knots[0] = (self.knots[0][0] + 1, self.knots[0][1])
        elif direction == "L":
            self.knots[0] = (self.knots[0][0] - 1, self.knots[0][1])
        else:
            print("incorrect direction")
            exit(1)

    @staticmethod
    def move_next_knot(current, next):
        diff = (current[0] - next[0], current[1] - next[1])
        # one directional cases
        if diff == (2, 0):
            next = (next[0] + 1, next[1])
        elif diff == (-2, 0):
            next = (next[0] - 1, next[1])
        elif diff == (0, 2):
            next = (next[0], next[1] + 1)
        elif diff == (0, -2):
            next = (next[0], next[1] - 1)
        # Diagonal cases
        elif diff == (2, 1) or diff == (1, 2) or diff == (2, 2):
            next = (next[0] + 1, next[1] + 1)
        elif diff == (2, -1) or diff == (1, -2) or diff == (2, -2):
            next = (next[0] + 1, next[1] - 1)
        elif diff == (-1, 2) or diff == (-2, 1) or diff == (-2, 2):
            next = (next[0] - 1, next[1] + 1)
        elif diff == (-1, -2) or diff == (-2, -1) or diff == (-2, -2):
            next = (next[0] - 1, next[1] - 1)
        return next

    def do_move(self, direction: str):
        self.move_head(direction)
        for i in range(1, len(self.knots)):
            self.knots[i] = Rope.move_next_knot(self.knots[i - 1], self.knots[i])
        self.tail_positions.add(self.knots[-1])

    def do_repeated_move(self, direction: str, times: int):
        for i in range(times):
            self.do_move(direction)


def puzzle1(data):
    rope = Rope(2)
    for move in data:
        rope.do_repeated_move(move[0], move[1])
    print("Puzzle 1: ", len(rope.tail_positions))


def puzzle2(data):
    rope = Rope(10)
    for move in data:
        rope.do_repeated_move(move[0], move[1])
    print("Puzzle 2: ", len(rope.tail_positions))


def parse_input(data):
    lines = data.strip().split("\n")
    return [(line.split(" ")[0], int(line.split(" ")[1])) for line in lines]


def main():
    with open("input/input_day09.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
