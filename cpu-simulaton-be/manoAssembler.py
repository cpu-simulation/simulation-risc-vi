class Assembler(object):
    
    def __init__(self, program):
        self.program = program

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
    
def hex_to_int(address):
    return int(address, 16)    