import intcode

import asyncio


async def puzzle1(program):
    async def simple_input():
        return 1

    async def simple_output(operand):
        print("Output: ", operand)

    computer = intcode.IntCodeComputer(program, simple_input, simple_output)
    await computer.run()


def puzzle2(data):
    pass


def main():
    with open("input/input_day9.txt") as f:
        data = f.read()
    program = [int(s.strip()) for s in data.split(",")]
    asyncio.run(puzzle1(program))


if __name__ == "__main__":
    main()
