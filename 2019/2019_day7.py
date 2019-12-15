import intcode

import asyncio
import itertools


async def run_amplifiers(program, phase_start, phase_end):
    loop = asyncio.get_event_loop()
    outputs = dict()
    number_computers = 5
    permutations = list(itertools.permutations(range(phase_start, phase_end + 1)))
    for phase_setting in permutations:
        queues = [asyncio.Queue(loop=loop) for i in range(number_computers)]

        def queue_input(queue: asyncio.Queue):
            return queue.get

        def queue_output(queue: asyncio.Queue):
            return queue.put

        for i in range(number_computers):
            setting = list(phase_setting)
            queues[i].put_nowait(setting[i])
        queues[0].put_nowait(0)

        computers = [
            intcode.IntCodeComputer(
                program,
                queue_input(queues[i]),
                queue_output(queues[(i + 1) % len(queues)]),
            )
            for i in range(number_computers)
        ]
        tasks = [asyncio.create_task(computer.run()) for computer in computers]
        await asyncio.gather(*tasks)
        outputs[phase_setting] = await queues[0].get()

    print("Highest output: ", max(outputs.values()))
    print("Phase setting: ", max(outputs, key=outputs.get))


async def puzzle1(program):
    await run_amplifiers(program, 0, 4)
    await run_amplifiers(program, 5, 9)


def main():
    with open("input/input_day7.txt") as f:
        data = f.read()
    program = [int(s.strip()) for s in data.split(",")]
    asyncio.run(puzzle1(program))


if __name__ == "__main__":
    main()
