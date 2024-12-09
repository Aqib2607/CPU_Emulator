import pytest
from src.assembler.assembler import Assembler

def test_assembler_conversion():
    assembler = Assembler()
    asm_code = "LOAD R1, 0x1000"
    machine_code = assembler.assemble(asm_code)
    expected_machine_code = "0xA000"  # Example machine code (replace with actual logic)
    assert machine_code == expected_machine_code, f"Expected {expected_machine_code} but got {machine_code}"

def test_invalid_assembly():
    assembler = Assembler()
    invalid_code = "INVALID R1, 0x1000"
    with pytest.raises(ValueError):
        assembler.assemble(invalid_code)
