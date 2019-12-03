def main():
    with open("input") as f:
        text = f.read()
        data = list(map(int, text.split(",")))

    pc = 0
    while True:
        if data[pc] == 1:
            data[data[pc+3]] = data[data[pc+1]]+data[data[pc+2]]
            pc += 4
        elif data[pc] == 2:
            data[data[pc+3]] = data[data[pc+1]]*data[data[pc+2]]
            pc += 4
        elif data[pc] == 99:
            break
    print(data[0])

main()
