import pytest
from src.cpu.alu import ALU
from src.cpu.registers import Registers

def test_alu_addition():
    alu = ALU()
    result = alu.add(5, 3)
    assert result == 8, f"Expected 8 but got {result}"

def test_alu_subtraction():
    alu = ALU()
    result = alu.subtract(5, 3)
    assert result == 2, f"Expected 2 but got {result}"

def test_registers_initialization():
    registers = Registers()
    assert registers.get_register('R1') == 0, "R1 should be initialized to 0"
    assert registers.get_register('R2') == 0, "R2 should be initialized to 0"
