import sys;rl=sys.stdin.readline
n = int(rl())
left = 0
right = 2e63
mid = (left+right)//2
while left < right:
    if mid**2 >= n:
        right = mid - 1
    elif mid**2 < n:
        left = mid + 1
    mid = (left+right)//2

print(int(mid))