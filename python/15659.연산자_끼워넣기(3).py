import sys;rl=sys.stdin.readline

operator = [0,0,0,0]

N = int(rl())
numbers = rl().rstrip().split()
max_operator = list(map(int,rl().split()))
Max = -1000000001
Min = 1000000001
tmp = [numbers[0]]

def dfs(num):
    if num==N:
        global Max,Min
        Max = max(Max,eval(''.join(tmp)))
        Min = min(Min,eval(''.join(tmp)))
        return
    for i in range(4):
        if operator[i] != max_operator[i]:
            operator[i]+=1
            if i == 0:
                tmp.append('+')
            elif i == 1:
                tmp.append('-')
            elif i == 2:
                tmp.append('*')
            else:
                tmp.append('//')
            tmp.append(numbers[num])
            dfs(num+1)
            tmp.pop()
            tmp.pop()
            operator[i]-=1

dfs(1)
print(Max)
print(Min)