from itertools import permutations
from day5 import main

if __name__ == "__main__":
    n = 0
    FILE = "input"
    for permutation in permutations(range(5,10)):
        print(permutation)
        input1 = list()
        input2 = list()
        input3 = list()
        input4 = list()
        input5 = list()

        machine1 = None
        machine2 = None
        machine3 = None
        machine4 = None
        machine5 = None
        
        input1.append(0)

        while True:
            try:
                if machine1 == None:
                    input1.append(permutation[0])
                    machine1 = main(FILE, inputs=input1)
                output1 = machine1.__next__()
                input2.append(output1)
                if machine2 == None:
                    input2.append(permutation[1])
                    machine2 = main(FILE, inputs=input2)
                output2 = machine2.__next__()
                input3.append(output2)
                if machine3 == None:
                    input3.append(permutation[2])
                    machine3 = main(FILE, inputs=input3)
                output3 = machine3.__next__()
                input4.append(output3)
                if machine4 == None:
                    input4.append(permutation[3])
                    machine4 = main(FILE, inputs=input4)
                output4 = machine4.__next__()
                input5.append(output4)
                if machine5 == None:
                    input5.append(permutation[4])
                    machine5 = main(FILE, inputs=input5)
                output5 = machine5.__next__()
                input1.append(output5)
            except:
                n = max(output5, n)
                break

    print(f"MAX: {n}")

