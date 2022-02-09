import sys

string = sys.stdin.readline().rstrip()
tmp = []
queue = []
plus_flag = 0

for i in string:
    if i.isdigit():
        tmp.append(i)
    else:
        queue.append(int(''.join(tmp)))
        tmp = []
        if i == '+' and plus_flag == 0:
            queue.append('+')
        else:
            queue.append('-')
            plus_flag = 1
queue.append(int(''.join(tmp)))

plus_flag = 0
ans = 0

for i in queue:
    if i == '+':
        plus_flag = 0
    elif i == '-':
        plus_flag = 1
    else:
        if plus_flag == 0:
            ans+=i
        else:
            ans-=i

print(ans)