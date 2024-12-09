; Program with branching logic
LOAD R1, 0x3000      ; Load value from memory
CMP R1, 5            ; Compare R1 with 5
BEQ label            ; Branch to 'label' if equal
ADD R2, R1, 1        ; If not equal, add 1 to R1 and store in R2
label:
STORE R2, 0x3001     ; Store result in memory
