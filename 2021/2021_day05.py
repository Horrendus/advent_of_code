from collections import defaultdict


def calculate_line_points(lines):
    line_points = defaultdict(lambda: 0)
    for line in lines:
        if line["x1"] == line["x2"]:
            x = line["x1"]
            y_min = min(line["y1"], line["y2"])
            y_max = max(line["y1"], line["y2"])
            for y in range(y_min, y_max + 1):
                line_points[(x, y)] += 1
        elif line["y1"] == line["y2"]:
            y = line["y1"]
            x_min = min(line["x1"], line["x2"])
            x_max = max(line["x1"], line["x2"])
            for x in range(x_min, x_max + 1):
                line_points[(x, y)] += 1
        else:
            # diagonal line
            x_stepping = 1 if line["x1"] < line["x2"] else -1
            y_stepping = 1 if line["y1"] < line["y2"] else -1
            x_coords = list(range(line["x1"], line["x2"] + x_stepping, x_stepping))
            y_coords = list(range(line["y1"], line["y2"] + y_stepping, y_stepping))
            for i in range(len(x_coords)):
                line_points[(x_coords[i], y_coords[i])] += 1
    return line_points


def puzzle1(data):
    filtered_lines = [
        line for line in data if line["x1"] == line["x2"] or line["y1"] == line["y2"]
    ]
    line_points = calculate_line_points(filtered_lines)
    points_multiple_lines = [
        point for point in line_points.keys() if line_points[point] >= 2
    ]
    print("Puzle 1: ", len(points_multiple_lines))


def puzzle2(data):
    line_points = calculate_line_points(data)
    points_multiple_lines = [
        point for point in line_points.keys() if line_points[point] >= 2
    ]
    print("Puzle 2: ", len(points_multiple_lines))


def parse_input(data):
    data = data.strip().split("\n")
    line_tuples = [line.split(" -> ") for line in data]
    lines = [
        {
            "x1": int(line[0].split(",")[0]),
            "y1": int(line[0].split(",")[1]),
            "x2": int(line[1].split(",")[0]),
            "y2": int(line[1].split(",")[1]),
        }
        for line in line_tuples
    ]
    return lines


def main():
    with open("input/input_day05.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
