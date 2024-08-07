import sys;rl=sys.stdin.readline

cond2 = list("abcdefghijklmnopqrstuvwxyz")
cond3 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
cond4 = list("1234567890")
cond5 = list("#@*&")

T = int(rl())
for t in range(T):
    N = int(rl())
    old = list(rl().strip())
    v1,v2,v3,v4,v5 = N >= 7,False,False,False,False
    for char in old:
        if v2 and v3 and v4 and v5:
            break
        
        if not v2 and char in cond2:
            v2 = True
            continue
        if not v3 and char in cond3:
            v3 = True
            continue
        if not v4 and char in cond4:
            v4 = True
            continue
        if not v5 and char in cond5:
            v5 = True
            continue
    
    if not v2:
        old.append(cond2[0])
    if not v3:
        old.append(cond3[0])
    if not v4:
        old.append(cond4[0])
    if not v5:
        old.append(cond5[0])
    
    old = ''.join(old)
    if(len(old) < 7):
        old += 'X' * (7-len(old))
    
    print('Case #' + str(t + 1) + ': ' + old)