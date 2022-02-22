from collections import deque
import sys;rl=sys.stdin.readline

while 1:
    inp = rl().rstrip()
    if inp == '0':
        break
    An = deque(list(map(int,inp.split())))
    n = An.popleft()
    #각 직사각형의 높이값을 의미하는 배열이 입력, An[0]은 직사각형의 갯수
    Stack = []
    Max = 0
    tmp = 0
    for i in range(n):
        if len(Stack):
            if An[Stack[-1]] > An[i]:
                while Stack:
                    if An[Stack[-1]] <= An[i]:
                        break
                    tmp = Stack.pop()
                    if Stack:
                        Max = max(Max,An[tmp] * (i - Stack[-1] - 1))
                    else:
                        Max = max(Max,i * An[tmp])
        Stack.append(i)
    
    while Stack:
        tmp = Stack.pop()
        if Stack:
            Max = max(Max,An[tmp] * (n - Stack[-1] - 1))
        else:
            Max = max(Max,An[tmp] * n)
    print(Max)