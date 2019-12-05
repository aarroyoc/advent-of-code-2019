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

def read(data, pc, mode):
    if mode == 1:
        return data[pc]
    else:
        try:
            return data[data[pc]]
        except:
            breakpoint()

def write(data, pc, mode, value):
    data[data[pc]] = value

def main():
    with open("input") as f:
        text = f.read()
        data = list(map(int, text.split(",")))
    pc = 0
    while True:
        op, mode_c, mode_b, mode_a = parse_opcode(data[pc])
        if op == 1:
            a = read(data, pc+1, mode_a)
            b = read(data, pc+2, mode_b)
            write(data, pc+3, 0, a+b)
            pc += 4
        elif op == 2:
            a = read(data, pc+1, mode_a)
            b = read(data, pc+2, mode_b)
            write(data, pc+3, 0, a*b)
            pc += 4
        elif op == 3:
            c = int(input("> "))
            write(data, pc+1, 0, c)
            pc += 2
        elif op == 4:
            c = read(data, pc+1, 0)
            print(c)
            pc += 2
        elif op == 5:
            a = read(data, pc+1, mode_a)
            b = read(data, pc+2, mode_b)
            if a != 0:
                pc = b
            else:
                pc += 3
        elif op == 6:
            a = read(data, pc+1, mode_a)
            b = read(data, pc+2, mode_b)
            if a == 0:
                pc = b
            else:
                pc += 3
        elif op == 7:
            a = read(data, pc+1, mode_a)
            b = read(data, pc+2, mode_b)
            if a < b:
                write(data, pc+3, mode_c, 1)
            else:
                write(data, pc+3, mode_c, 0)
            pc += 4
        elif op == 8:
            a = read(data, pc+1, mode_a)
            b = read(data, pc+2, mode_b)
            if a == b:
                write(data, pc+3, mode_c, 1)
            else:
                write(data, pc+3, mode_c, 0)
            pc += 4
        elif data[pc] == 99:
            break

main()
