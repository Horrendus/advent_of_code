import intcode

import asyncio


async def puzzle1(program):
    async def simple_input():
        return 1

    async def simple_output(operand):
        print("Output: ", operand)

    computer = intcode.IntCodeComputer(program, simple_input, simple_output)
    await computer.run()


async def puzzle2(program):
    async def simple_input():
        return 2

    async def simple_output(operand):
        print("Output: ", operand)

    computer = intcode.IntCodeComputer(program, simple_input, simple_output)
    await computer.run()


def main():
    with open("input/input_day9.txt") as f:
        data = f.read()
    program = [int(s.strip()) for s in data.split(",")]
    asyncio.run(puzzle1(program))
    asyncio.run(puzzle2(program))


if __name__ == "__main__":
    main()
