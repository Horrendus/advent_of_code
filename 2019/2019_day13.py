import intcode
import asyncio


async def puzzle1(program):
    out = []

    async def simple_output(operand):
        out.append(operand)

    computer = intcode.IntCodeComputer(program, None, simple_output)
    await computer.run()
    triples = []
    for i in range(0, len(out) - 2, 3):
        triples.append((out[i], out[i + 1], out[i + 2]))
    blocks = [triple for triple in triples if triple[2] == 2]
    print("Blocks: ", len(blocks))


def puzzle2(data):
    pass


def parse_input(data):
    pass


def main():
    with open("input/input_day13.txt") as f:
        data = f.read()
    program = [int(s.strip()) for s in data.split(",")]
    asyncio.run(puzzle1(program))
    puzzle2(data)


if __name__ == "__main__":
    main()
