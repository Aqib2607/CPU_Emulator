# src/cpu/alu.py

class ALU:
    def __init__(self):
        # Define operation types
        self.operations = {
            "ADD": self.add,
            "SUB": self.subtract,
            "MUL": self.multiply,
            "DIV": self.divide,
            "AND": self.and_op,
            "OR": self.or_op,
            "XOR": self.xor_op
        }

    def add(self, operand1, operand2):
        return operand1 + operand2

    def subtract(self, operand1, operand2):
        return operand1 - operand2

    def multiply(self, operand1, operand2):
        return operand1 * operand2

    def divide(self, operand1, operand2):
        if operand2 == 0:
            raise ValueError("Cannot divide by zero.")
        return operand1 / operand2

    def and_op(self, operand1, operand2):
        return operand1 & operand2

    def or_op(self, operand1, operand2):
        return operand1 | operand2

    def xor_op(self, operand1, operand2):
        return operand1 ^ operand2

    def execute(self, operation, operand1, operand2):
        if operation in self.operations:
            return self.operations[operation](operand1, operand2)
        else:
            raise ValueError(f"Operation {operation} not supported.")
