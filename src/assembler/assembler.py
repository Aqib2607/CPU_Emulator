# src/assembler/assembler.py

class Assembler:
    def __init__(self):
        self.instructions = {
            "ADD": "0001",
            "SUB": "0010",
            "LOAD": "0100",
            "STORE": "0101",
        }

    def assemble(self, assembly_code):
        # Convert the assembly code into machine code
        machine_code = []
        for instruction in assembly_code:
            op, *operands = instruction.split()
            machine_code.append(self.instructions.get(op, "0000") + ''.join(operands))
        return machine_code

    def disassemble(self, machine_code):
        # Convert machine code back to assembly (optional)
        assembly_code = []
        for code in machine_code:
            op = code[:4]
            operands = code[4:]
            assembly_code.append(self.reverse_lookup(op) + " " + operands)
        return assembly_code

    def reverse_lookup(self, opcode):
        # Reverse lookup for opcode
        for op, code in self.instructions.items():
            if code == opcode:
                return op
        return "UNKNOWN"
