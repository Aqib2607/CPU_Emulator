# src/cpu/instruction_cycle.py

class InstructionCycle:
    def __init__(self, alu, registers):
        self.alu = alu
        self.registers = registers
        self.program_counter = 0
        self.instruction_register = None

    def fetch(self, instruction_memory):
        # Simulate fetching an instruction from memory
        if self.program_counter < len(instruction_memory):
            self.instruction_register = instruction_memory[self.program_counter]
            self.program_counter += 1
        else:
            raise ValueError("Program counter out of bounds.")

    def decode(self):
        # Decode the instruction (example: ADD, SUB, etc.)
        if self.instruction_register is None:
            raise ValueError("No instruction to decode.")
        operation, operand1, operand2 = self.instruction_register
        return operation, operand1, operand2

    def execute(self, operation, operand1, operand2):
        # Execute the operation using ALU
        return self.alu.execute(operation, operand1, operand2)

    def cycle(self, instruction_memory):
        # Complete the fetch-decode-execute cycle
        self.fetch(instruction_memory)
        operation, operand1, operand2 = self.decode()
        return self.execute(operation, operand1, operand2)
