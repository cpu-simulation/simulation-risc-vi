from math import log
from flask import Flask, request
from flask_cors import CORS

class Computer(object):

    def __init__(self, program):
        self.program = program
        self.ram = Memory(1024 * 4)     # 4K RAM
        self.ar = Register(12)          # Address register
        self.pc = Register(12)          # Program counter
        self.dr = Register(16)          # Data register
        self.ac = Register(16)          # Accumulator
        self.ir = Register(16)          # Instruction register
        self.tr = Register(16)          # Temporary register
        self.inpr = Register(8)         # Input register
        self.outr = Register(8)         # Output register
        self.sc = Register(3)           # Sequence counter
        self.e = Register(1)            # Carry bit
        self.s = Register(1)            # Start / stop computer
        self.fgi = Register(1)          # Input register available
        self.fgo = Register(1)          # Output register available


        
    # Memory reference
    mri = {
            'AND': 0x0000,
            'ADD': 0x1000,
            'LDA': 0x2000,
            'STA': 0x3000,
            'BUN': 0x4000,
            'BSA': 0x5000,
            'ISZ': 0x6000,
            
            'ANDI': 0X8000,
            'ADDI': 0X9000,
            'LDAI': 0XA000,
            'STAI': 0XB000,
            'BUNI': 0XC000,
            'BSAI': 0XD000,
            'ISZI': 0XE000

        }

        # Register reference
    rri = {
            'CLA': 0x7800,
            'CLE': 0x7400,
            'CMA': 0x7200,
            'CME': 0x7100,
            'CIR': 0x7080,
            'CIL': 0x7040,
            'INC': 0x7020,
            'SPA': 0x7010,
            'SNA': 0x7008,
            'SZA': 0x7004,
            'SZE': 0x7002,
            'HLT': 0x7001
        }

        # Input / output
    io = {
            'INP': 0xF800,
            'OUT': 0xF400,
            'SKI': 0xF200,
            'SKO': 0xF100,
            'ION': 0xF080,
            'IOF': 0xF040
        } 
    


   

    def compile(self, memory): # Compiles and loades the instructions
        location = 0
        programStart = None
        for(command, operand, indirect) in self.lines():
            if command == 'ORG':
                location = hex_to_int(operand)
                if programStart is None:
                    programStart = location
                continue

            elif command == 'HEX':
                instruction = hex_to_int(operand)
            
            
            elif command in self.mri:
                instruction = self.mri[command]
                if indirect:
                    instruction |= (1 << 15)

            elif command in self.rri:
                instruction = self.rri[command]

            elif command in self.io:
                instruction = self.io[command]

            else:
                raise SyntaxError("Unrecognized command: '%s'" % command)

            memory.write(location, instruction)
            location += 1

        return programStart
    
    def lines(self):  # Generative method
        for line in self.program.split('\n'):
            line = line.strip()

            if line == '':
                continue

            if line == 'END':
                break

            yield self.parseLine(line)


    @staticmethod
    def parseLine(line):
        parts = line.split()
        command = parts.pop(0)
        operand = None
        indirect = False
        if command.endswith('I'):
            indirect = True
            command = command[:-1]
        if parts:
            operand = parts.pop(0)
        return command, operand, indirect
    
    def run(self, program_start):
        self.pc.word = program_start
        self.s.word = 1
        while self.s.word == 1:
            self.tick()
    
    def tick(self):
        t = self.sc.word
        d = self.get_opcode()
        i = self.get_indirect_bit()

        if t < 3:
            self.interrupt(t)

        if t < 2:
            self.instruction_fetch(t)

        if t == 2:
            self.instruction_decode()

        if t == 3 and d != 7:
            self.operand_fetch(i)

        if t > 3 and d != 7:
            self.execute_mri(d, t)

        if t == 3 and d == 7:
            b = self.get_instruction_bit()
            if i:
                self.execute_io(b)
            else:
                self.execute_rri(b)
    
    def get_opcode(self):
        """
        Number in IR(12-14)
        """
        return (self.ir.word >> 12) & 7

    def get_indirect_bit(self):
        """
        IR(15) bit
        """
        return (self.ir.word >> 15) & 1

    def get_instruction_bit(self):
        """
        Bit in IR(0-11) that specifies the operation
        """
        return log(self.ir.word & 0xFFF, 2)
    
    def instruction_fetch(self, t):
        if t == 0:
            # R'T0: AR <- PC
            self.ar.word = self.pc.word
            self.sc.increment()
        elif t == 1:
            # R'T1: IR <- M[AR], PC <- PC + 1
            self.memory_read(self.ir)
            self.pc.increment()
            self.sc.increment()

    def instruction_decode(self):
        # R'T2: AR <- IR(0-11)
        self.ar.word = self.ir.word & 0xFFF
        self.sc.increment()

    def operand_fetch(self, i):
        if i:
            # D7'I'T3: NOOP
            self.memory_read(self.ar)

        # D7'I'T3: NOOP
        self.sc.increment()

    def execute_mri(self, d, t):
        if d == 0:
            self.execute_and(t)
        elif d == 1:
            self.execute_add(t)
        elif d == 2:
            self.execute_lda(t)
        elif d == 3:
            self.execute_sta()
        elif d == 4:
            self.execute_bun()
        elif d == 5:
            self.execute_bsa(t)
        elif d == 6:
            self.execute_isz(t)

    def execute_rri(self, b):
        if b == 11:
            self.execute_cla()
        elif b == 10:
            self.execute_cle()
        elif b == 9:
            self.execute_cma()
        elif b == 8:
            self.execute_cme()
        elif b == 7:
            self.execute_cir()
        elif b == 6:
            self.execute_cil()
        elif b == 5:
            self.execute_inc()
        elif b == 4:
            self.execute_spa()
        elif b == 3:
            self.execute_sna()
        elif b == 2:
            self.execute_sza()
        elif b == 1:
            self.execute_sze()
        elif b == 0:
            self.execute_hlt()

        self.sc.clear()

    def execute_io(self, b):
        if b == 11:
            self.execute_inp()
        elif b == 10:
            self.execute_out()
        elif b == 9:
            self.execute_ski()
        elif b == 8:
            self.execute_sko()
        elif b == 7:
            self.execute_ion()
        elif b == 6:
            self.execute_iof()

        self.sc.clear()
    
    def execute_and(self, t):
        if t == 4:
            # D0T4: DR <- M[AR]
            self.memory_read(self.dr)
            self.sc.increment()
        elif t == 5:
            # D0T5: AC <- AC & DR, SC <- 0
            self.ac.logic_and(self.dr.word)
            self.sc.clear()

    def execute_add(self, t):
        if t == 4:
            # D1T4: DR <- M[AR]
            self.memory_read(self.dr)
            self.sc.increment()
        elif t == 5:
            # D1T5: AC <- AC + DR, E <- Cout, SC <- 0
            self.e.word = self.ac.add(self.dr.word)
            self.sc.clear()

    def execute_lda(self, t):
        if t == 4:
            # D2T4: DR <- M[AR]
            self.memory_read(self.dr)
            self.sc.increment()
        elif t == 5:
            # D2T4: AC <- DR, SC <- 0
            self.ac.word = self.dr.word
            self.sc.clear()

    def execute_sta(self):
        # D3T4: M[AR] <- AC, SC <- 0
        self.memory_write(self.ac)
        self.sc.clear()

    def execute_bun(self):
        # D4T4: PC <- AR, SC <- 0
        self.pc.word = self.ar.word
        self.sc.clear()

    def execute_bsa(self, t):
        if t == 4:
            # D5T4: M[AR] <- PC, AR <- AR + 1
            self.memory_write(self.pc)
            self.ar.increment()
            self.sc.increment()
        elif t == 5:
            # D5T5: PC <- AR, SC <- 0
            self.pc.word = self.ar.word
            self.sc.clear()

    def execute_isz(self, t):
        if t == 4:
            # D6T4: DR <- M[AR]
            self.memory_read(self.dr)
            self.sc.increment()
        elif t == 5:
            # D6T5: DR <- DR + 1
            self.dr.increment()
            self.sc.increment()
        elif t == 6:
            # D6T6: M[AR] <- DR, if (DR = 0) then (PC <- PC + 1), SC <- 0
            self.memory_write(self.dr)
            if self.dr.word == 0:
                self.pc.increment()
            self.sc.clear()

    def execute_cla(self):
        # D7I'T3B11: AC <- 0, SC <- 0
        self.ac.clear()

    def execute_cle(self):
        # D7I'T3B10: E <- 0, SC <- 0
        self.e.clear()

    def execute_cma(self):
        # D7I'T3B9: AC <- AC', SC <- 0
        self.ac.complement()

    def execute_cme(self):
        # D7I'T3B8: E <- E', SC <- 0
        self.e.complement()

    def execute_cir(self):
        # D7I'T3B7: AC <- shr(AC), AC(15) <- E, E <- AC(0), SC <- 0
        self.e.word = self.ac.shift_right(self.e.word)

    def execute_cil(self):
        # D7I'T3B6: AC <- shl(AC), AC(0) <- E, E <- AC(15), SC <- 0
        self.e.word = self.ac.shift_left(self.e.word)

    def execute_inc(self):
        # D7I'T3B5: AC <- AC + 1, SC <- 0
        self.ac.increment()

    def execute_spa(self):
        # D7I'T3B4: if (AC(15) = 0) then (PC <- PC + 1), SC <- 0
        if not self.ac.word & 0x800:
            self.pc.increment()

    def execute_sna(self):
        # D7I'T3B3: if (AC(15) = 1) then (PC <- PC + 1), SC <- 0
        if self.ac.word & 0x800:
            self.pc.increment()

    def execute_sza(self):
        # D7I'T3B2: if (AC = 0) then (PC <- PC + 1), SC <- 0
        if self.ac.word == 0:
            self.pc.increment()

    def execute_sze(self):
        # D7I'T3B1: if (E = 0) then (PC <- PC + 1), SC <- 0
        if self.e.word == 0:
            self.pc.increment()

    def execute_hlt(self):
        # D7I'T3B0: S <- 0, SC <- 0
        self.s.word = 0

    def execute_inp(self):
        # D7IT3B11: AC(0-7) <- INPR, FGI <- 0
        self.ac.word &= 0xFF00
        self.ac.word |= self.inpr.word
        self.fgi.clear()

    def execute_out(self):
        # D7IT3B10: OUTR <- AC(0-7), FGO <- 0
        self.outr.word = self.ac.word & 0xFF
        self.fgo.clear()

    def execute_ski(self):
        # D7IT3B9: if (FGI = 1) then (PC <- PC + 1)
        if self.fgi.word == 1:
            self.pc.increment()


    def execute_sko(self):
        # D7IT3B8: if (FGO = 1) then (PC <- PC + 1)
        if self.fgo.word == 1:
            self.pc.increment()

    
    def read_register(self):
        registers = {
            'AR': self.ar.word,
            'PC': self.pc.word,
            'DR': self.dr.word,
            'AC': self.ac.word,
            'IR': self.ir.word,
            'TR': self.tr.word,
            'INPR': self.inpr.word,
            'OUTR': self.outr.word,
            'SC': self.sc.word,
            'E': self.e.word,
            'S': self.s.word,
            'FGI': self.fgi.word,
            'FGO': self.fgo.word
        }
        return registers        
    
    def memory_read(self, source_register):
        source_register.word = self.ram.read(self.ar.word)

    def memory_write(self, target_register):
        self.ram.write(self.ar.word, target_register.word)








    
    

def hex_to_int(address):
    return int(address, 16)
                    


class Register(object):
    
    def __init__(self, bits):
        self.bits = bits
        self.word = 0
        self.maxValue = 1 << self.bits
        self.mask = self.maxValue - 1

    def increment(self):
        self.word = (self.word + 1) % self.maxValue

    def clear(self):
        self.word = 0

    def logic_and(self, word):
        self.word &= word

    def add(self, word):
        value = self.word + word
        carry = value & self.maxValue
        self.word = value % self.maxValue

        return 1 if carry else 0

    def complement(self):
        self.word = ~self.word & self.mask

    def shift_right(self, msb):
        lsb = self.word & 1
        self.word >>= 1
        if msb:
            maskMSB = self.maxValue >> 1
            self.word |= maskMSB

        return lsb

    def shift_left(self, lsb):
        msb_mask = self.maxValue >> 1
        msb = 1 if self.word & msb_mask else 0
        self.word = (self.word << 1) & self.mask
        if lsb:
            self.word |= 1

        return msb

    def __str__(self):
        return 'Register(word=%s)' % bin(self.word)[2:].zfill(self.bits)


class Memory(object):
    def __init__(self):
        self.memory = {}

    def write(self, address, data):
        self.memory[address] = data
    
    def read(self, address):
        return self.memory.get(address, None)
    
    def readBulkMemory(self):
        return str(self.memory)
    
    def writeBulk(self, bulkData):
        for address, data in bulkData.items():
            self.write(address, data)

########################################
#############api########################
########################################

computer = ""

api = Flask(__name__)

CORS(api)

@api.route("/memory/write", methods=["POST"])
def writeMemory():
    if request.method == 'POST':
        json = request.json
        address = json.get("address")
        value = json.get("value")
        print(address, value)
        return ('', 204)

@api.route("/memory/bulk_write", methods=["POST"])
def bulkWrite():
    if request.method == "POST":
        json = request.json
        data = json.get("data")
        return ('', 204)
    
@api.route("/memory/read/<address>")
def read(address):
    pass 

@api.route("/memory/bulk_read/<bulk_address>")
def bulkRead(bulk_address):
    pass

@api.route("/register/write", methods=["POST"])
def writeRegister():
    return ('', 204) 

@api.route("/register/read")
def readRegister():
    print(computer.read_register())
    return ('', 204)

@api.route("/core/execute",methods=["POST"])
def execute():
    return ('', 204)

@api.route("/core/compile",methods=["GET", "POST"])
def compile():
    if request.method == "POST":
        json = request.json
        instructions = json.get("instructions")
        print(instructions)
        computer = Computer(instructions)
        print(json)
        return ('', 204)

if __name__ == "__main__":
  api.run(host="localhost", port="8000", debug=True)