import sys


class Map:
    def __init__(self, raw_input):
        self.wirepositions = dict()
        self.directions = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
        self.wires = self.parse_wires(raw_input)

    @staticmethod
    def parse_wires(raw_input):
        wires = []
        for line in raw_input:
            if line:
                wires.append(line.strip().split(","))
        return wires

    def run_wires(self):
        for i in range(len(self.wires)):
            self.run_wire(self.wires[i], i)

    def run_wire(self, wire, number):
        current_coordinate = (0, 0)
        current_pos = 0
        current_steps = 0
        while True:
            direction = self.directions[wire[current_pos][0]]
            no_of_steps = int(wire[current_pos][1:])
            for i in range(1, no_of_steps + 1):
                current_coordinate = (
                    current_coordinate[0] + direction[0],
                    current_coordinate[1] + direction[1],
                )
                current_steps += 1
                if current_coordinate in self.wirepositions:
                    if number not in self.wirepositions[current_coordinate]["wires"]:
                        self.wirepositions[current_coordinate]["wires"].append(number)
                        self.wirepositions[current_coordinate][
                            "total_length"
                        ] += current_steps
                else:
                    self.wirepositions[current_coordinate] = {
                        "wires": [number],
                        "total_length": current_steps,
                    }
            current_pos += 1
            if current_pos == len(wire):
                break


def puzzle1(data):
    m = Map(data)
    m.run_wires()
    closest_crossing_distance = sys.maxsize
    closest_intersection_length = sys.maxsize
    for key, value in m.wirepositions.items():
        if len(value["wires"]) > 1 and key != (0, 0):
            distance = abs(key[0]) + abs(key[1])
            if distance < closest_crossing_distance:
                closest_crossing_distance = min(distance, closest_crossing_distance)
            if value["total_length"] < closest_intersection_length:
                closest_intersection_length = value["total_length"]

    print("Puzzle 1: ", closest_crossing_distance)
    print("Puzzle 2: ", closest_intersection_length)


def puzzle2(data):
    # both implemented in puzzle1
    pass


def main():
    with open("input/input_day3.txt") as f:
        data = f.readlines()
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
