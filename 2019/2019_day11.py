import intcode
import asyncio

DIRECTIONS = ["up", "right", "down", "left"]


class PanelControl:
    def __init__(self, white_start=False):
        self.current_position = (0, 0)
        self.current_direction = 0
        self.panels = dict()
        self.first_input = True
        if white_start:
            self.panels[self.current_position] = True

    async def robot_input(self):
        if (
            self.current_position in self.panels.keys()
            and self.panels[self.current_position]
        ):
            return 1
        return 0

    async def robot_output(self, value):
        if self.first_input:
            if value == 1:
                self.panels[self.current_position] = True
            else:
                self.panels[self.current_position] = False
            self.first_input = False
        else:
            if value == 0:
                # turn left
                self.current_direction = (self.current_direction - 1) % len(DIRECTIONS)
            else:
                # turn right
                self.current_direction = (self.current_direction + 1) % len(DIRECTIONS)
            # move one
            move_direction = DIRECTIONS[self.current_direction]
            if move_direction == "up":
                self.current_position = (
                    self.current_position[0] + 0,
                    self.current_position[1] + 1,
                )
            elif move_direction == "right":
                self.current_position = (
                    self.current_position[0] + 1,
                    self.current_position[1] + 0,
                )
            elif move_direction == "down":
                self.current_position = (
                    self.current_position[0] + 0,
                    self.current_position[1] - 1,
                )
            elif move_direction == "left":
                self.current_position = (
                    self.current_position[0] - 1,
                    self.current_position[1] + 0,
                )
            self.first_input = True

    def number_painted_panels(self):
        return len(self.panels)

    def paint_panels(self):
        min_x = min(self.panels.keys(), key=lambda t: t[0])[0]
        min_y = min(self.panels.keys(), key=lambda t: t[1])[1]
        max_x = max(self.panels.keys(), key=lambda t: t[0])[0]
        max_y = max(self.panels.keys(), key=lambda t: t[1])[1]
        for y in range(max_y + 1, min_y, -1):
            line = ""
            for x in range(min_x, max_x + 1):
                if (x, y) in self.panels and self.panels[(x, y)]:
                    line += "*"
                else:
                    line += " "
            print(line)


async def puzzle1(program):
    control = PanelControl()

    computer = intcode.IntCodeComputer(
        program, control.robot_input, control.robot_output
    )
    await computer.run()
    print("Number of Panels painted at least once: ", control.number_painted_panels())


async def puzzle2(program):
    control = PanelControl(white_start=True)

    computer = intcode.IntCodeComputer(
        program, control.robot_input, control.robot_output
    )
    await computer.run()
    control.paint_panels()


def parse_input(data):
    pass


def main():
    with open("input/input_day11.txt") as f:
        data = f.read()
    program = [int(s.strip()) for s in data.split(",")]
    asyncio.run(puzzle1(program))
    asyncio.run(puzzle2(program))


if __name__ == "__main__":
    main()
