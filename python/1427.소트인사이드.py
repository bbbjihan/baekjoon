import sys;rl=sys.stdin.readline
N = list(rl().rstrip())
N.sort(reverse=True)
print(int(''.join(N)))