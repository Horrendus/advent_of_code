UNIQUE_NUMBERS_SEGMENTS = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}


def puzzle1(data):
    count_1478 = 0
    for entry in data:
        for outputs in entry[1]:
            if len(outputs) in UNIQUE_NUMBERS_SEGMENTS.keys():
                count_1478 += 1
    print("Puzzle 1: ", count_1478)


def calculate_output(seg_out, numbers_for_wires):
    numbers = []
    for seg in seg_out:
        numbers.append(numbers_for_wires[seg])
    output_num = int("".join([str(n) for n in numbers]))
    return output_num


def puzzle2(data):
    sum = 0
    for entry in data:
        wire_mapping = {}
        wires_for_number = {}
        seg_in = entry[0]
        seg_out = entry[1]
        wires_for_number[1] = seg_in[0]
        assert len(wires_for_number[1]) == 2
        wires_for_number[4] = seg_in[2]
        assert len(wires_for_number[4]) == 4
        wires_for_number[7] = seg_in[1]
        assert len(wires_for_number[7]) == 3
        wires_for_number[8] = seg_in[9]
        assert len(wires_for_number[8]) == 7
        wire_a = [
            wire for wire in wires_for_number[7] if wire not in wires_for_number[1]
        ]
        assert len(wire_a) == 1
        wire_mapping["a"] = wire_a[0]
        assert wires_for_number[7] == "".join(
            sorted(wires_for_number[1] + wire_mapping["a"])
        )
        wires_069 = seg_in[6:9]
        assert all([len(i) == 6 for i in wires_069])
        for wires in wires_069:
            if not all([wire in wires for wire in wires_for_number[1]]):
                break
        wire_c = [wire for wire in wires_for_number[1] if wire not in wires]
        assert len(wire_c) == 1
        wires_for_number[6] = wires
        wire_mapping["c"] = wire_c[0]
        wire_f = [wire for wire in wires_for_number[1] if wire != wire_mapping["c"]]
        assert len(wire_f) == 1
        wire_mapping["f"] = wire_f[0]
        wires_09 = [wires for wires in wires_069 if wires != wires_for_number[6]]
        wires_bd = [
            wire
            for wire in wires_for_number[4]
            if wire != wire_mapping["c"] and wire != wire_mapping["f"]
        ]
        assert len(wires_bd) == 2
        for wires in wires_09:
            if not all([wire in wires for wire in wires_bd]):
                break
        wire_d = [wire for wire in wires_bd if wire not in wires]
        assert len(wire_d) == 1
        wire_mapping["d"] = wire_d[0]
        wire_b = [wire for wire in wires_bd if wire != wire_mapping["d"]]
        assert len(wire_b) == 1
        wire_mapping["b"] = wire_b[0]
        wires_for_number[0] = wires
        wires_09.remove(wires)
        assert len(wires_09) == 1
        wires_for_number[9] = wires_09[0]
        wires_235 = seg_in[3:6]
        assert all([len(i) == 5 for i in wires_235])
        for wires in wires_235:
            if not wire_mapping["f"] in wires:
                break
        wires_for_number[2] = wires
        wire_e = [
            wire for wire in wires_for_number[8] if wire not in wires_for_number[9]
        ]
        assert len(wire_e) == 1
        wire_mapping["e"] = wire_e[0]
        wire_g = [
            wire for wire in wires_for_number[8] if wire not in wire_mapping.values()
        ]
        assert len(wire_g) == 1
        wire_mapping["g"] = wire_g[0]
        # we have all mappings but continue with numbers so that we can be sure its correct
        wires_35 = [wires for wires in wires_235 if wires != wires_for_number[2]]
        wires_3 = [wires for wires in wires_35 if not wire_mapping["b"] in wires]
        assert len(wires_3) == 1
        wires_for_number[3] = wires_3[0]
        wires_35.remove(wires_for_number[3])
        assert len(wires_35) == 1
        wires_for_number[5] = wires_35[0]
        number_for_wires = dict((v, k) for k, v in wires_for_number.items())
        sum += calculate_output(seg_out, number_for_wires)

    print("Puzzle 2: ", sum)


def parse_input(data):
    lines = data.strip().split("\n")
    unsorted_data = [
        (
            line.split(" | ")[0].split(" "),
            line.split(" | ")[1].split(" "),
        )
        for line in lines
    ]
    sorted_data = []
    for seg_in, seg_out in unsorted_data:
        sorted_data.append(
            (
                sorted(["".join(sorted(seg)) for seg in seg_in], key=len),
                ["".join(sorted(seg)) for seg in seg_out],
            )
        )
    return sorted_data


def main():
    with open("input/input_day08.txt") as f:
        data = f.read()
    data = parse_input(data)
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
