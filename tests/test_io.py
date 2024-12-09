import pytest
from src.cpu.io import IO

def test_io_input():
    io = IO()
    io.input_data = "Test Input"
    result = io.read_input()
    assert result == "Test Input", f"Expected 'Test Input' but got {result}"

def test_io_output():
    io = IO()
    io.write_output("Test Output")
    result = io.get_output()
    assert result == "Test Output", f"Expected 'Test Output' but got {result}"
