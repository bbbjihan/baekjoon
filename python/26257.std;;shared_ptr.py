import sys;rl=sys.stdin.readline

N,M,Q = map(int,rl().split())

pointers = [0]
for _ in range(M):
    pointers.append(int(rl()))

def assign(x, y):
    pointers[x] = pointers[y]

def swap(x, y):
    pointers[x], pointers[y] = pointers[y], pointers[x]

def reset(x):
    pointers[x] = 0

for _ in range(Q):
    command = rl().split()
    if command[0] =='assign':
        assign(int(command[1]), int(command[2]))
    elif command[0] == 'swap':
        swap(int(command[1]), int(command[2]))
    else:
        reset(int(command[1]))

memories = list(set(pointers))
memories.sort()

print(len(memories) - 1 if 0 in memories else len(memories))
for memory in memories:
    if memory > 0:
        print(memory)