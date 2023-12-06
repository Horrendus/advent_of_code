import math


def calculate_races(races):
    record_beating_ways = []
    for i in range(len(races)):
        records_beaten = 0
        time, distance = races[i]
        for starting_speed in range(1, time):
            distance_moved = starting_speed * (time - starting_speed)
            if distance_moved > distance:
                records_beaten += 1
        record_beating_ways.append(records_beaten)
    return math.prod(record_beating_ways)


def puzzle1(races):
    print("Puzzle 1: ", calculate_races(races))


def puzzle2(races):
    long_time = int("".join([str(race[0]) for race in races]))
    long_distance = int("".join([str(race[1]) for race in races]))
    long_race = (long_time, long_distance)
    # this is definitly not the intended way to solve this because this takes ~ 6 s to finish
    # TODO: figure out the real math behind this :)
    print("Puzzle 2: ", calculate_races([long_race]))


def parse_input(data):
    lines = data.strip().split("\n")
    times = [int(x) for x in lines[0].split(" ")[1:] if x]
    distances = [int(x) for x in lines[1].split(" ")[1:] if x]
    return [(times[i], distances[i]) for i in range(len(times))]


def main():
    with open("input/input_day06.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
