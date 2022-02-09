import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()

def compare_Pn(str,n):
    for i in range(n):
        if i%2 == 0 and str[i] == 'O':
            return False
        elif i%2 == 1 and str[i] == 'I':
            return False
    return True


cnt = 0
for i in range(M-2*N):
    if compare_Pn(string[i:i+2*N+1],2*N+1):
        cnt+=1

print(cnt)