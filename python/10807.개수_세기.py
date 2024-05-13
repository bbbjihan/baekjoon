import sys;rl=sys.stdin.readline

N = int(rl())
arr = list(map(int,rl().split()))
v = int(rl())

cnt = 0
for num in arr:
  if num == v:
    cnt += 1

print(cnt)