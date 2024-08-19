import sys;rl=sys.stdin.readline

while True:
    N = int(rl())
    if N == 0:
        break
    
    pos = 0
    for _ in range(N):
        li = list(rl().strip())
        if pos >= len(li):
            continue
        now = li[pos]
        while pos < len(li) and now != ' ':
            pos += 1
            if pos == len(li):
                break
            now = li[pos]
    
    print(pos + 1)