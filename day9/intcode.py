def parse_opcode(opcode):
    opcode = str(opcode)
    if len(opcode) > 1:
        instruction = int(opcode[-2:])
        try:
            mode_a = int(opcode[-3])
        except:
            mode_a = 0
        try:
            mode_b = int(opcode[-4])
        except:
            mode_b = 0
        try:
            mode_c = int(opcode[-5])
        except:
            mode_c = 0
    else:
        instruction = int(opcode)
        mode_c = 0
        mode_b = 0
        mode_a = 0
    return (instruction, mode_c, mode_b, mode_a)

class Memory:
    def __init__(self):
        self.base = 0

    def set_base(self, base):
        self.base += base

    def read(self, data, pc, mode):
        if mode == 2:
            address = self.base+data[pc]
        elif mode == 1:
            address = pc
        else:
            address = data[pc]

        try:
            return data[address]
        except IndexError:
            while address >= len(data):
                data.append(0)
            return data[address]

    def write(self, data, pc, mode, value):
        if mode == 2:
            address = self.base+data[pc]
        elif mode == 1:
            address = pc
        else:
            address = data[pc]

        try:
            data[address] = value
        except IndexError:
            while address >= len(data):
                data.append(0)
            data[address] = value


def main(in_file, inputs):
    with open(in_file) as f:
        text = f.read()
        data = list(map(int, text.split(",")))
    pc = 0
    r = Memory()
    outputs = list()
    while True:
        op, mode_c, mode_b, mode_a = parse_opcode(data[pc])
        if op == 1:
            a = r.read(data, pc+1, mode_a)
            b = r.read(data, pc+2, mode_b)
            r.write(data, pc+3, mode_c, a+b)
            pc += 4
        elif op == 2:
            a = r.read(data, pc+1, mode_a)
            b = r.read(data, pc+2, mode_b)
            r.write(data, pc+3, mode_c, a*b)
            pc += 4
        elif op == 3:
            if len(inputs) > 0:
                c = inputs.pop()
            else:
                c = int(input("> "))
            r.write(data, pc+1, mode_a, c)
            pc += 2
        elif op == 4:
            c = r.read(data, pc+1, mode_a)
            yield c
            pc += 2
        elif op == 5:
            a = r.read(data, pc+1, mode_a)
            b = r.read(data, pc+2, mode_b)
            if a != 0:
                pc = b
            else:
                pc += 3
        elif op == 6:
            a = r.read(data, pc+1, mode_a)
            b = r.read(data, pc+2, mode_b)
            if a == 0:
                pc = b
            else:
                pc += 3
        elif op == 7:
            a = r.read(data, pc+1, mode_a)
            b = r.read(data, pc+2, mode_b)
            if a < b:
                r.write(data, pc+3, mode_c, 1)
            else:
                r.write(data, pc+3, mode_c, 0)
            pc += 4
        elif op == 8:
            a = r.read(data, pc+1, mode_a)
            b = r.read(data, pc+2, mode_b)
            if a == b:
                r.write(data, pc+3, mode_c, 1)
            else:
                r.write(data, pc+3, mode_c, 0)
            pc += 4
        elif op == 9:
            a = r.read(data, pc+1, mode_a)
            r.set_base(a)
            pc += 2
        elif data[pc] == 99:
            break
    return

if __name__ == "__main__":
    main("input")
