from collections import defaultdict

def main():
    with open("input") as f:
        wire1 = f.readline().split(",")
        wire2 = f.readline().split(",")
    matrix = defaultdict(lambda: 1)
    steps1 = defaultdict(lambda: 0)
    steps2 = defaultdict(lambda: 0)

    x = 0
    y = 0
    step = 0
    for cmd in wire1:
        move = int(cmd[1:])
        if cmd[0] == "R":
            for n in range(1,move+1):
                matrix[(x+n,y)] *= 3
                steps1[(x+n,y)] = step
                step += 1
            x += move
        elif cmd[0] == "U":
            for n in range(1, move+1):
                matrix[(x, y+n)] *= 3
                steps1[(x, y+n)] = step
                step += 1
            y += move
        elif cmd[0] == "L":
            for n in range(1, move+1):
                matrix[(x-n, y)] *= 3
                steps1[(x-n, y)] = step
                step += 1
            x -= move
        elif cmd[0] == "D":
            for n in range(1, move+1):
                matrix[(x, y-n)] *= 3
                steps1[(x, y-n)] = step
                step += 1
            y -= move

    x = 0
    y = 0
    step = 0
    for cmd in wire2:
        move = int(cmd[1:])
        if cmd[0] == "R":
            for n in range(1, move+1):
                matrix[(x+n,y)] *= 2
                steps2[(x+n,y)] = step
                step += 1
            x += move
        elif cmd[0] == "U":
            for n in range(1, move+1):
                matrix[(x, y+n)] *= 2
                steps2[(x, y+n)] = step
                step += 1
            y += move
        elif cmd[0] == "L":
            for n in range(1, move+1):
                matrix[(x-n, y)] *= 2
                steps2[(x-n,y)] = step
                step += 1
            x -= move
        elif cmd[0] == "D":
            for n in range(1, move+1):
                matrix[(x, y-n)] *= 2
                steps2[(x, y-n)] = step
                step += 1
            y -= move

    min_dist = None
    min_step = None
    for crosses in matrix:
        if matrix[crosses] % 6 == 0:
            x,y = crosses
            
            if min_dist == None or min_dist > abs(x) + abs(y):
                min_dist = abs(x) + abs(y)

            if min_step == None or min_step > steps1[crosses]+steps2[crosses]+2:
                min_step = steps1[crosses] + steps2[crosses]+2

    print("Min Dist: ", min_dist)
    print("Min Step: ", min_step)

            
        
            
        
main()