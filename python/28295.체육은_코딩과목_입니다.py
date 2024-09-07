import sys;rl=sys.stdin.readline

d = 0
for _ in range(10):
    c = int(rl())
    if c == 1:
        d += 1
    elif c == 2:
        d += 2
    else:
        d -= 1

r = ["N", "E", "S", "W"]

print(r[d%4])