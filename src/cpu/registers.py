# src/cpu/registers.py

class Registers:
    def __init__(self, num_registers=8):
        # Initialize a set of registers, default to 8 registers
        self.registers = [0] * num_registers

    def read(self, register_id):
        if register_id < 0 or register_id >= len(self.registers):
            raise ValueError("Invalid register ID.")
        return self.registers[register_id]

    def write(self, register_id, value):
        if register_id < 0 or register_id >= len(self.registers):
            raise ValueError("Invalid register ID.")
        self.registers[register_id] = value
