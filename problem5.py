def div(num):
    r = 1
    stop = False
    while not stop and r <= 20:
        if num % r == 0:
            r = r + 1
        else:
            stop = True
    if r == 21:
        return True
    if stop:
        return False


def solution():
    num = 2520
    while not div(num):
        num = num + 1
    return num

print(solution())
