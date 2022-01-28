import sys
n = int(sys.stdin.readline())
for i in range(n):
    S = [False for i in range(20)]
    command = sys.stdin.readline().split()
    if command[0] == 'add':
        S[int(command[1])-1]=True
    elif command[0] == 'remove':
        S[int(command[1])-1]=False
    elif command[0] == 'check':
        if S[int(command[1])-1]:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        S[int(command[1])-1]=not(S[int(command[1])-1])
    elif command[0] == 'all':
        S = [True for i in range(20)]
    elif command[0] == 'empty':
        S = [False for i in range(20)]