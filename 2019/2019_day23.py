import intcode
import asyncio
import sys

from typing import Tuple

number_computers = 50


class InputTracker:
    def __init__(self, num):
        print(f"IT {num} initializing")
        self.queue = [num]
        self.num = num

    def put_value(self, value: Tuple[int, int]):
        print(f"IT {self.num}: received packet: {value[0]},{value[1]}")
        self.queue.append(value[0])
        self.queue.append(value[1])

    async def get_value(self):
        if len(self.queue) == 0:
            val = -1
            await asyncio.sleep(1)
        else:
            val = self.queue.pop(0)
            print(f"IT {self.num}: value for Computer: {val}")

        return val


input_trackers = [InputTracker(i) for i in range(number_computers)]


class OutputTracker:
    def __init__(self, num):
        print(f"OT {num} initializing")
        self.dest = 0
        self.count = 0
        self.cached_value = -1
        self.num = num

    async def add(self, value):
        if self.count == 0:
            print(f"OT {self.num}, new dest: {value}")
            self.dest = value
        if self.count == 1:
            print(f"OT {self.num}, count: {self.count} put value to cache: {value}")
            self.cached_value = value
        if self.count == 2:
            print(
                f"OT {self.num}, count: {self.count} put packet to dest {self.dest}: {self.cached_value},{value}"
            )
            if self.dest >= 0 and self.dest < 50:
                input_trackers[self.dest].put_value((self.cached_value, value))
            if self.dest == 255:
                print(
                    f"OT {self.num}, count: {self.count} put packet for 255: {self.cached_value},{value}"
                )
                sys.exit(0)

            self.cached_value = -1

        self.count = (self.count + 1) % 3


output_trackers = [OutputTracker(i) for i in range(number_computers)]


async def puzzle1(program):
    computers = [
        intcode.IntCodeComputer(
            program,
            input_trackers[i].get_value,
            output_trackers[i].add,
        )
        for i in range(number_computers)
    ]
    tasks = [asyncio.create_task(computer.run()) for computer in computers]
    await asyncio.gather(*tasks)


def puzzle2(data):
    pass


def parse_input(data):
    pass


def main():
    with open("input/input_day23.txt") as f:
        data = f.read()
    program = [int(s.strip()) for s in data.split(",")]
    asyncio.run(puzzle1(program))
    puzzle2(data)


if __name__ == "__main__":
    main()
