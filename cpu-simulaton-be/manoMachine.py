from math import log
from math import log


class Computer(object):
    def __init__(self):
        self.ram = Memory(1024 * 4)     # 4K RAM
        self.ar = Register(12)          # Address register
        self.pc = Register(12)          # Program counter
        self.dr = Register(16)          # Data register
        self.ac = Register(16)          # Accumulator
        self.ir = Register(16)          # Instruction register
        self.tr = Register(16)          # Temp register
        self.inpr = Register(8)         # Input register
        self.outr = Register(8)         # Output register
        self.sc = Register(3)           # Sequence counter
        self.e = Register(1)            # Carry bit
        self.s = Register(1)            # Start / stop computer
        self.r = Register(1)            # Interrupt raised
        self.ien = Register(1)          # Interrupt enable
        self.fgi = Register(1)          # Input register available
        self.fgo = Register(1)          # Output register available

    def run(self, program_start):
        self.pc.word = program_start
        self.s.word = 1
        while self.s.word == 1:
            self.tick()

    def tick(self):
        t = self.sc.word
        r = self.r.word
        d = self.get_opcode()
        i = self.get_indirect_bit()

        if t < 3 and r == 1:
            self.interrupt(t)

        if t < 2 and r == 0:
            self.instruction_fetch(t)

        if t == 2 and r == 0:
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

    def interrupt(self, t):
        if t == 0:
            # RT0: AR <- 0, TR <- PC
            self.ar.clear()
            self.tr.word = self.pc.word
            self.sc.increment()
        elif t == 1:
            # RT1: M[AR] <- TR, PC <- 0
            self.memory_write(self.tr)
            self.pc.clear()
            self.sc.increment()
        elif t == 2:
            # RT2: PC <- PC + 1, IEN <- 0, R <- 0, SC <- 0
            self.pc.increment()
            self.ien.clear()
            self.r.clear()
            self.sc.clear()

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
            # D7'IT3: AR <- M[AR]
            self.memory_read(self.ar)
        # else:
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

    def execute_ion(self):
        # D7IT3B7: IEN <- 1
        self.ien.word = 1

    def execute_iof(self):
        # D7IT3B6: IEN <- 0
        self.ien.clear()
    
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


class Register(object):
    def __init__(self, bits):
        self.bits = bits
        self.word = 0
        self.max_value = 1 << self.bits
        self.mask = self.max_value - 1

    def increment(self):
        self.word = (self.word + 1) % self.max_value

    def clear(self):
        self.word = 0

    def logic_and(self, word):
        self.word &= word

    def add(self, word):
        value = self.word + word
        carry = value & self.max_value
        self.word = value % self.max_value

        return 1 if carry else 0

    def complement(self):
        self.word = ~self.word & self.mask

    def shift_right(self, msb):
        lsb = self.word & 1
        self.word >>= 1
        if msb:
            msb_mask = self.max_value >> 1
            self.word |= msb_mask

        return lsb

    def shift_left(self, lsb):
        msb_mask = self.max_value >> 1
        msb = 1 if self.word & msb_mask else 0
        self.word = (self.word << 1) & self.mask
        if lsb:
            self.word |= 1

        return msb

    def __str__(self):
        return 'Register(word=%s)' % bin(self.word)[2:].zfill(self.bits)


class Memory(object):
    def __init__(self, size):
        self.size = size
        self.data = [0] * size

    def write(self, address, word):
        self.data[address] = word

    def read(self, address):
        return self.data[address]

    def __str__(self):
        return 'Memory(size=%dK)' % (self.size / 1024)
        
    def bulk_read(self):
        non_zero_cells = [[addr, self.data[addr]] for addr in range(self.size) if self.data[addr] != 0]
        return non_zero_cells
    


########################################
#############api########################
########################################

computer = Computer

