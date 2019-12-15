from typing import List, Tuple


class IntCodeComputer:
    def __init__(self, program: List[int], input_function, output_function):
        self.sp = 0
        self.relative_base = 0
        self.program = program.copy()
        self.input_function = input_function
        self.output_function = output_function
        self.is_running = True

        self.function_map = {
            99: self.finish,
            1: self.add,
            2: self.multiply,
            3: self.input,
            4: self.output,
            5: self.jmp_nzero,
            6: self.jmp_zero,
            7: self.lt_other,
            8: self.eq_other,
            9: self.adj_relative_base,
        }

    async def finish(self, _):
        self.is_running = False

    def write_memory(self, operand, address):
        if len(self.program) <= address:
            self.program.extend([0] * (1 + address - len(self.program)))
        self.program[address] = operand

    def read_memory(self, address) -> int:
        if len(self.program) <= address:
            return 0
        return self.program[address]

    async def input(self, opcode_list):
        operand1 = self.read_memory(self.sp + 1)
        # operand1 = (
        #     operand1
        #     if opcode_list[2] == 1
        #     else self.relative_base + operand1
        #     if opcode_list[2] == 1
        #     else self.read_memory(operand1)
        # )
        res = await self.input_function()
        self.write_memory(res, operand1)
        self.sp += 2

    async def output(self, opcode_list):
        operand1 = self.get_one_operand(opcode_list)
        await self.output_function(operand1)
        self.sp += 2

    async def add(self, opcode_list):
        operand1, operand2, operand3 = self.get_three_operands(opcode_list)
        res = operand1 + operand2
        self.write_memory(res, operand3)
        self.sp += 4

    async def multiply(self, opcode_list):
        operand1, operand2, operand3 = self.get_three_operands(opcode_list)
        res = operand1 * operand2
        self.write_memory(res, operand3)
        self.sp += 4

    async def jmp_nzero(self, opcode_list):
        operand1, operand2 = self.get_two_operands(opcode_list)
        if operand1 != 0:
            self.sp = operand2
        else:
            self.sp += 3

    async def jmp_zero(self, opcode_list):
        operand1, operand2 = self.get_two_operands(opcode_list)
        if operand1 == 0:
            self.sp = operand2
        else:
            self.sp += 3

    async def lt_other(self, opcode_list):
        operand1, operand2, operand3 = self.get_three_operands(opcode_list)
        res = operand1 < operand2
        self.write_memory(int(res), operand3)
        self.sp += 4

    async def eq_other(self, opcode_list):
        operand1, operand2, operand3 = self.get_three_operands(opcode_list)
        res = operand1 == operand2
        self.write_memory(int(res), operand3)
        self.sp += 4

    async def adj_relative_base(self, opcode_list):
        operand1 = self.get_one_operand(opcode_list)
        self.relative_base += operand1
        self.sp += 2

    def get_one_operand(self, opcode_list):
        param_mode_1 = opcode_list[2]
        operand1 = self.read_memory(self.sp + 1)
        operand1, _, _ = self.parameter_translation(operand1, 0, 0, param_mode_1, 0, 0)
        return operand1

    def get_two_operands(self, opcode_list):
        param_mode_1 = opcode_list[2]
        param_mode_2 = opcode_list[1]
        operand1 = self.read_memory(self.sp + 1)
        operand2 = self.read_memory(self.sp + 2)
        op1, op2, _ = self.parameter_translation(
            operand1, operand2, 0, param_mode_1, param_mode_2, 0
        )
        return op1, op2

    def get_three_operands(self, opcode_list):
        param_mode_1 = opcode_list[2]
        param_mode_2 = opcode_list[1]
        param_mode_3 = opcode_list[0]
        operand1 = self.read_memory(self.sp + 1)
        operand2 = self.read_memory(self.sp + 2)
        operand3 = self.read_memory(self.sp + 3)
        operand1, operand2, operand3 = self.parameter_translation(
            operand1, operand2, operand3, param_mode_1, param_mode_2, param_mode_3
        )
        return operand1, operand2, operand3

    def parameter_translation(
        self, operand1, operand2, operand3, param_mode_1, param_mode_2, param_mode_3
    ) -> Tuple[int, int]:
        op1 = (
            operand1
            if param_mode_1 == 1
            else self.read_memory(self.relative_base + operand1)
            if param_mode_2 == 2
            else self.read_memory(operand1)
        )
        op2 = (
            operand2
            if param_mode_2 == 1
            else self.read_memory(self.relative_base + operand2)
            if param_mode_2 == 2
            else self.read_memory(operand2)
        )
        # op3 = (
        #     operand3
        #     if param_mode_3 == 1
        #     else self.relative_base + operand3
        #     if param_mode_3 == 2
        #     else self.read_memory(operand3)
        # )
        return op1, op2, operand3

    @staticmethod
    def parse_opcode(opcode):
        opcode = str(opcode).zfill(5)
        opcode_list = [int(code) for code in list(opcode)]
        last = opcode_list.pop()
        second_last = opcode_list.pop()
        opcode_list.append(second_last * 10 + last)
        return opcode_list

    async def run(self):
        while self.is_running:
            opcode = self.program[self.sp]
            opcode_list = self.parse_opcode(opcode)
            await self.function_map[opcode_list[3]](opcode_list)
