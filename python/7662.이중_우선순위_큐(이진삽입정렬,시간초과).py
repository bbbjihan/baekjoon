import sys
from collections import deque

T = int(sys.stdin.readline())

def insert(queue:deque,num:int):
    if len(queue) == 0:
        queue.append(num)
    else:
        flag = 0
        left = 0
        right = len(queue)-1
        while left<=right:
            mid = (left+right)//2
            if queue[mid] == num:
                break
            elif queue[mid] > num:
                right = mid-1
                flag = 0
            else:
                left = mid+1
                flag = 1
        if flag == 1:
            queue.insert(mid+1,num)
        else:
            queue.insert(mid,num)


def delete(queue:deque,num:int):
    if len(queue) == 0:
        return
    elif num == 1:
        queue.pop()
    else:
        queue.popleft()


for _ in range(T):
    N = int(sys.stdin.readline())
    queue = deque()
    for _ in range(N):
        command = sys.stdin.readline().rstrip().split()
        if command[0] == 'I':
            insert(queue,int(command[1]))
        else:
            if command[1] == '1':
                delete(queue,1)
            else:
                delete(queue,-1)
    
    if len(queue) == 0:
        print('EMPTY')
    else:
        print(str(queue[len(queue)-1]) + ' ' + str(queue[0]))