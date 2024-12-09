# Instruction Set Architecture (ISA)

## Week 2: Instruction Set Architecture (ISA)

### Objective:
- Design the ISA for the virtual CPU.

### Tasks:
1. **Define basic instructions**:
   - `ADD`: Adds two values in registers and stores the result in a register.
   - `SUB`: Subtracts one register value from another.
   - `LOAD`: Loads data from memory into a register.
   - `STORE`: Stores data from a register into memory.
   - More instructions can be added later based on project progression.

2. **Document the instruction formats**:
   - Each instruction will consist of an operation code (opcode) and operands, e.g., `ADD R1, R2, R3` (adds values in R2 and R3, stores result in R1).

3. **Create a simple assembler**:
   - The assembler will read assembly code and convert it into machine code that the virtual CPU can execute.
