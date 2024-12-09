; Program to simulate I/O operations
LOAD R1, 0x2000      ; Load value from I/O register (simulated) into R1
OUT R1               ; Output value in R1 to I/O device
IN R2                ; Read input from I/O device into R2
STORE R2, 0x2001     ; Store input into memory
