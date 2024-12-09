# src/main.py

from cpu.alu import ALU
from cpu.registers import Registers
from cpu.instruction_cycle import InstructionCycle
from cpu.memory import Memory
from cpu.io import IO
from assembler.assembler import Assembler
from utils.profiler import Profiler
from utils.logger import log

def main():
    # Setup components
    alu = ALU()
    registers = Registers()
    memory = Memory()
    io = IO()
    assembler = Assembler()
    profiler = Profiler()

    profiler.start()

    # Example instruction sequence (assembler)
    assembly_code = [
        "LOAD 0x1000",
        "ADD 0x1001, 10",
        "STORE 0x1002"
    ]
    
    machine_code = assembler.assemble(assembly_code)
    log(f"Machine Code: {machine_code}")

    # Create instruction cycle and execute
    instruction_cycle = InstructionCycle(alu, registers)
    for instruction in machine_code:
        result = instruction_cycle.cycle([instruction])
        log(f"Execution Result: {result}")
    
    profiler.stop()

if __name__ == "__main__":
    main()
