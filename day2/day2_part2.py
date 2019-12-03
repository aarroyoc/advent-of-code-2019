def main():
    for i in range(100):
        for j in range(100):
            with open("input") as f:
                text = f.read()
                data = list(map(int, text.split(",")))
            data[1] = i
            data[2] = j
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
            if data[0] == 19690720:
                print("I", i)
                print("J", j)
                print("Output: ", 100*i + j )

main()
