import sys;rl=sys.stdin.readline

operator = [0,0,0,0]

N = int(rl())
numbers = list(map(int,rl().split()))
max_operator = list(map(int,rl().split()))
Max = -1000000001
Min = 1000000001
pretmp = 0

def dfs(num,tmp):
    if num==N:
        global Max,Min
        Max = max(Max,tmp)
        Min = min(Min,tmp)
        return
    for i in range(4):
        if operator[i] < max_operator[i]:
            operator[i]+=1
            if i == 0:
                dfs(num+1,tmp+numbers[num])
            elif i == 1:
                dfs(num+1,tmp-numbers[num])
            elif i == 2:
                dfs(num+1,tmp*numbers[num])
            else:
                if tmp < 0:
                    dfs(num+1,-((-tmp)//numbers[num]))
                else:
                    dfs(num+1,tmp//numbers[num])
            operator[i]-=1

dfs(1,numbers[0])
print(Max)
print(Min)