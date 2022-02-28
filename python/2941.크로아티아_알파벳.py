import sys;rl=sys.stdin.readline

st = rl().rstrip()
leng = len(st)
cnt = 0
ansLeng = leng
i = 0
while i < leng:
    if st[i] == 'c' and i < leng-1:
        if st[i+1] == '=':
            cnt+=1
            ansLeng-=2
            i+=1
        elif st[i+1] == '-':
            cnt+=1
            ansLeng-=2
            i+=1
    if st[i] == 'd' and i < leng-2:
        if st[i+1] == 'z' and st[i+2] == '=' :
            cnt+=1
            ansLeng-=3
            i+=2
    if st[i] == 'd' and i < leng-1:
        if st[i+1] == '-':
            cnt+=1
            ansLeng-=2
            i+=1
    if st[i] == 'l' and i < leng-1:
        if st[i+1] == 'j':
            cnt+=1
            ansLeng-=2
            i+=1
    if st[i] == 'n' and i < leng-1:
        if st[i+1] == 'j':
            cnt+=1
            ansLeng-=2
            i+=1
    if st[i] == 's' and i < leng-1:
        if st[i+1] == '=':
            cnt+=1
            ansLeng-=2
            i+=1
    if st[i] == 'z' and i < leng-1:
        if st[i+1] == '=':
            cnt+=1
            ansLeng-=2
            i+=1
    i+=1

print(cnt+ansLeng)