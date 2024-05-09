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
    seq = rl().rstrip() # string
    left,right,c = 0,0,0
    stack = []
    while 1:
        if right == len(seq):
            break
        if not stack:
            stack.append(seq[right])
        elif stack[-1] == '(' and seq[right] == ')':
            stack.pop()
        else:
            stack.append(seq[right])

        if left == right:
            right+=1
            continue

        prefixSeq = seq[left:right+1]
        if not stack or isPalindromes(prefixSeq):
            right+=1
            left = right
            c+=1
            stack.clear()
            continue

        
        right+=1
    print(c, right-left)