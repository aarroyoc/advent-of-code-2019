minx = 382345
maxx = 843167

def valid(password):
    p = str(password)
    a = p[0]
    b = p[1]
    c = p[2]
    d = p[3]
    e = p[4]
    f = p[5]
    repeat = 0
    repeat_group = False

    if a <= b:
        if a == b:
            repeat += 1
        if b <= c:
            if b == c:
                repeat += 1
            else:
                if repeat == 1:
                    repeat_group = True
                repeat = 0
            if c <= d:
                if c == d:
                    repeat += 1
                else:
                    if repeat == 1:
                        repeat_group = True
                    repeat = 0
                if d <= e:
                    if d == e:
                        repeat += 1
                    else:
                        if repeat == 1:
                            repeat_group = True
                        repeat = 0
                    if e <= f:
                        if e == f:
                            repeat += 1
                        else:
                            if repeat == 1:
                                repeat_group = True
                            repeat = 0
                        if repeat == 1:
                                repeat_group = True
                        return True and repeat_group
    return False

if __name__ == "__main__":
    n = 0
    for password in range(minx, maxx+1):
        if valid(password):
            n += 1

    print(f"Passwords: {n}")
