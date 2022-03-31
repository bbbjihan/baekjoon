from collections import deque
import sys;rl=sys.stdin.readline

def isPalindromes(sequence):
    if len(sequence) == 1:
        return False
    mid = len(sequence)//2
    a = ''.join(sequence)
    b = ''.join(reversed(sequence))
    if a[:mid] == b[:mid]:
        return True
    else:
        return False

T = int(rl())
for _ in range(T):
    N = int(rl())
    seq = deque(rl().rstrip())
    prefixSeq = []
    stack = []
    c = 0

    while seq:
        tmp = seq.popleft()
        prefixSeq.append(tmp)
        if not stack:
            stack.append(tmp)
        elif stack[-1] == '(' and tmp == ')':
            stack.pop()
        else:
            stack.append(tmp)
        
        if isPalindromes(prefixSeq) or not stack:
            prefixSeq = []
            stack = []
            c+=1
    
    print(c,len(prefixSeq))