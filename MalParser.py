''' Mini Asessembly languge MAL parser program
Created by Michael Roach
Feb 8 2018'''

class Parser:

    import datetime
    opcode_inval = 0

    def __init__(self, filename):
        # self.datetime = datetime
        self.filename = filename
        self.file = open(filename, 'r')
        logfile = filename[0:filename.index('.')]
        self.log = open(logfile+'.log', 'w')

        self.file = open(filename, 'r')
        self.opcodes = {'MOVE': ['s','d'],
                        'MOVEI': ['v','d'],
                        'ADD': ['s','s','d'],
                        'INC': ['s'],
                        "SUB": ['s','s','d'],
                        "DEC": ['s'],
                        "MUL": ['s','s','d'],
                        "DIV": ['s','s','d'],
                        "BEQ": ['s','s','l'],
                        "BLT": ['s','s','l'],
                        "BGT": ['s','s','l'],
                        "BR": ['l'],
                        "END": []}
        self.registers = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7']
        self.opcode_inval = 0
        self.operand_less = 0
        self.operand_more = 0
        self.operand_ill = 0
        self.operand_bad = 0

    def comment(self, line):
        if ';' in line:
            line = line[0:line.index(';')]
        return line

    def called(self, called_labels, instruction_list, idx):
        BGT ='BGT'
        BLT = 'BLT'
        BEQ = 'BEQ'
        BR = 'BR'
        label = instruction_list[0]
        if label == BR:
            called_labels.update({instruction_list[1]: [0, idx]})
        elif label == BLT:
            called_labels.update({instruction_list[3]: [0, idx]})
        elif label == BEQ:
            called_labels.update({instruction_list[3]: [0, idx]})
        elif label == BGT:
            called_labels.update({instruction_list[3]: [0, idx]})
        return called_labels

    def created(self, line, created_labels, idx):

        if ':' in line:
            created_labels.update({line[0:line.index(':')]: [0, idx]})
            line = line[line.index(':')+1:]
            if len(line) > 2:
                line = line.strip()
                return line
            return line
        else:
            return line

    def check_opcode(self, line, opcode, operands, instruction_list):

        print instruction_list
        print
        print '______________________________'
        opcode_keys = self.opcodes.iterkeys()
        key_list = self.opcodes.keys()
        op_valid = True

        if opcode in opcode_keys:
            print 'opcode valid'
            print operands
            print 'len of value list'
            print len(self.opcodes.get(opcode))
            key_list = self.opcodes.get(opcode)
            parser.check_operands(operands, key_list)
        else:
            parser.check_operands(operands, key_list)
            self.opcode_inval += 1
            print opcode
        print '__________________________________'

    def check_operands(self, operands, key_list):
        for item in key_list:
            # s =
            # d =
            # v =
            # l =
            pass

    def mal_checker(self):
        self.log.write('_________________________________________________________________\n')
        self.log.write('Error output for '+filename+'\n')
        self.log.write('_________________________________________________________________\n')
        lines = self.file.readlines()


        created_labels = {}
        called_labels = {}
        for idx, line in enumerate(lines):
            line = parser.comment(line)
            if line is "":
                continue
            self.log.write(str(idx) + line)
            if 'END' in line:
                continue
            line = line.strip()
            line = parser.created(line, created_labels, idx)
                # created_labels = parser.created(line, created_labels, idx)
            opcode = line[:line.find(' ')]
            oplength = len(opcode)
            instruction = line[oplength:]
            instruction = instruction.strip()
            operands = instruction.split(', ' or ' ')
            instruction_list = [opcode] + operands
            parser.called(called_labels, instruction_list, idx)
            if opcode == '':
                continue
            parser.check_opcode(line, opcode, operands, instruction_list)

            # print '-----------------------------------end of for ---------------------------------------'
            # self.log.flush()


        print created_labels
        print called_labels
        self.log.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
        self.log.write('Total errors - \n')
        self.log.write(' Invalid Opcode \n')
        self.log.write(' Too few Operands \n')
        self.log.write(' Too many operands \n')
        self.log.write(' Ill-formed Operand \n')
        self.log.write(' Wrong operand type \n')
        self.log.write(' Label Warnings \n')
        self.log.write('Mal error checker Complete ---- Mal program is ')
        print('exited for loop')


        self.file.close()
        self.log.close()
        print self.opcode_inval



if __name__ == '__main__':

        input = raw_input("Please enter the name of the file you would like to check for errors:")
        try:
            filename = input                                     #open('/Users/Roach/PycharmProjects/Mal_Log/one.mal', 'r')
            parser = Parser(filename)
            parser.mal_checker()


        except IOError:
            print 'file not found make sure the file is in the same folder'
            exit('No File')

# TODO recursive search if time
