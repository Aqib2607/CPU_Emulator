import pytest
from src.cpu.memory import Memory

def test_memory_read_write():
    memory = Memory()
    memory.write(0x1000, 123)
    result = memory.read(0x1000)
    assert result == 123, f"Expected 123 but got {result}"

def test_memory_out_of_bounds():
    memory = Memory()
    with pytest.raises(IndexError):
        memory.write(0x10000, 123)  # Assuming 0x10000 is out of bounds
