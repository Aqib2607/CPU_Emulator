# src/cpu/io.py

class IO:
    def __init__(self):
        self.input_buffer = []
        self.output_buffer = []

    def read_input(self):
        if self.input_buffer:
            return self.input_buffer.pop(0)
        else:
            raise ValueError("Input buffer is empty.")

    def write_output(self, value):
        self.output_buffer.append(value)

    def simulate_input(self, value):
        self.input_buffer.append(value)

    def get_output(self):
        return self.output_buffer
