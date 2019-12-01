import math

def operation1(x):
    x = int(x)
    x /= 3
    x = math.floor(x)
    x -= 2
    return x

def operation2(x):
    out = 0
    x = int(x)
    while x > 0:
        x = int(x)
        x /= 3
        x = math.floor(x)
        x -= 2
        if x > 0:
            out += x
    return out


with open("input") as f:
    lines = f.readlines()
    numbers = [operation1(x) for x in lines]
    output = sum(numbers)
    print(f"{output}")
