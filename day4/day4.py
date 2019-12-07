min = 382345
max = 843167

def consecutive(password):
    repeat = False
    a = int(password[0])
    b = int(password[1])
    c = int(password[2])
    d = int(password[3])
    e = int(password[4])
    f = int(password[5])
    if a <= b:
        if a == b:
            repeat = True
        if b <= c:
            if b == c:
                repeat = True
            if c <= d:
                if c == d:
                    repeat = True
                if d <= e:
                    if d == e:
                        repeat = True
                    if e <= f:
                        if e == f:
                            repeat = True
                        return repeat
    return False
n = 0
for password in range(min, max+1):
    if consecutive(str(password)):
        n += 1
print(f"Password: {n}")