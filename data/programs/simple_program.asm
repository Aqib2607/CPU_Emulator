; Simple program to add two numbers

LOAD R1, 0x1000      ; Load value from memory address 0x1000 into register R1
ADD R2, R1, 10       ; Add 10 to value in R1 and store in R2
STORE R2, 0x1001     ; Store value from R2 into memory address 0x1001
