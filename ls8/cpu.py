"""CPU functionality."""

import sys

JNE = 0b01010110
JEQ = 0b01010101
CMP = 0b10100111
JMP = 0b01010100
ADD = 0b10101000
RET = 0b00010001
HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010
POP = 0b01000110
PUSH = 0b01000101
CALL = 0b01010000

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0]*8
        self.ram = [0]*256
        self.reg[7] = 0xF4
        self.halted = False
        self.pc = 0
        self.SP = 7
        self.flag = 0b00000000

    def ram_read(self, location):
        """Return value at given Address"""
        return self.ram[location]
    
    def ram_write(self, location, value):
        """Write to a location in Memmory"""
        self.ram[location] = value

    def load(self, filename):
        """Load a program into memory.""" 
        address = 0
        pg_len = 0
        with open(filename) as fp:
            for line in fp:
                line_split = line.split("#")
                num = line_split[0].strip()
                if num == "":
                    continue
                val = int(num, 2)
                self.ram_write(address, val)
                address += 1
                pg_len += 1
        self.program_end = pg_len - 1
        self.reg
        


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op =="MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        elif op =="CMP":
            if reg_a == reg_b:
                self.flag == 0b00000001
            elif reg_a < reg_b:
                self.flag == 0b00000100
            elif reg_a > reg_b:
                self.flag == 0b00000010
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while self.halted != True:
            instruction_to_execute = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)
            self.execute_instruction(instruction_to_execute, operand_a, operand_b)
            
    def execute_instruction(self, instruction, operand_a, operand_b):
        if instruction == ADD:
            self.alu("ADD", operand_a, operand_b)
            self.pc += 3
        if instruction == HLT:
            self.halted = True
            self.pc += 1
        elif instruction == LDI:
            self.reg[operand_a] = operand_b
            self.pc += 3
        elif instruction == PRN:
            print(self.reg[operand_a])
            self.pc += 2
        elif instruction == MUL:
            self.alu("MUL", operand_a, operand_b)
            self.pc +=3
        elif instruction == PUSH:
            self.reg[self.SP] -= 1
            register_value = self.reg[operand_a]
            self.ram[self.reg[self.SP]] = register_value
            self.pc += 2
        elif instruction == POP:
            top = self.ram[self.reg[self.SP]]
            self.reg[operand_a] = top
            self.reg[self.SP] += 1
            self.pc += 2
        elif instruction == CALL:
            self.reg[self.SP] -= 1
            self.ram[self.reg[self.SP]] = operand_b
            self.pc += 2
        elif instruction == RET:
            return_address = self.ram[self.reg[self.SP]]
            self.ram[self.reg[self.SP]] += 1
            self.pc = return_address
        elif instruction == CMP:
            print("CMP CALLED")
            self.alu("CMP", operand_a, operand_b)
            self.pc += 3
        elif instruction == JMP:
            print("JMP CALLED")
            self.pc = self.reg[operand_a]
        elif instruction == JEQ:
            print("JEQ CALLED")
            if self.flag == 0b00000001:
                self.pc == self.reg[operand_a]
            else:
                self.pc += 2
        elif instruction == JNE:
            print("{0:b}".format(operand_a))
            print(operand_a)
            if self.flag == 0b00000000:
                print("THEY NOT")
                self.pc = self.reg[operand_a]
                print("{0:b}".format(self.pc))
            else:
                self.pc += 2
        
            


