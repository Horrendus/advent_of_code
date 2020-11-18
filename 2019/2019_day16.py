import math

BASE_PATTERN = [0, 1, 0, -1]


def create_pattern(pos, num_len):
    pattern = []
    for x in BASE_PATTERN:
        pattern.extend([x] * pos)
    pattern = pattern * math.ceil(num_len / len(pattern))
    return pattern[1 : num_len + 1]


def apply_pattern(num, pattern) -> int:
    digits = [int(d) for d in str(num)]
    full = sum([a * b for a, b in zip(digits, pattern)])
    result = abs(full) % 10
    return result


def do_phase(num, patterns) -> str:
    results = []
    for i in range(0, len(num)):
        results.append(apply_pattern(num, patterns[i]))
    return "".join(map(str, results))


def puzzle1(data):
    fft_phases = 100
    patterns = []
    num_len = len(data)
    for i in range(num_len):
        patterns.append(create_pattern(i + 1, num_len))
    fft_num = data
    for i in range(fft_phases):
        fft_num = do_phase(fft_num, patterns)
    print(fft_num[:8])


def puzzle2(data):
    pass


def parse_input(data):
    pass


def main():
    with open("input/input_day16.txt") as f:
        data = f.read()
    puzzle1(data)
    puzzle2(data)


if __name__ == "__main__":
    main()
