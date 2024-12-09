# src/cpu/memory.py

class Memory:
    def __init__(self, size=1024):
        # Default memory size 1024 units
        self.memory = [0] * size

    def read(self, address):
        if address < 0 or address >= len(self.memory):
            raise ValueError("Invalid memory address.")
        return self.memory[address]

    def write(self, address, value):
        if address < 0 or address >= len(self.memory):
            raise ValueError("Invalid memory address.")
        self.memory[address] = value
