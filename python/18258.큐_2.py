from collections import deque
import sys;rl=sys.stdin.readline

N = int(rl())
queue = deque()


for _ in range(N):
    Com = rl().rstrip().split()
    if Com[0] == 'push':
        queue.append(Com[1])
    elif Com[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif Com[0] == 'size':
        print(len(queue))
    elif Com[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif Com[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif Com[0] == 'back':
        if queue:
            print(queue[len(queue)-1])
        else:
            print(-1)