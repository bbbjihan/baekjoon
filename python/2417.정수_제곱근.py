import sys;rl=sys.stdin.readline
n = int(rl())
left = 0
right = n
mid = (left+right)//2
while left <= right:
    if mid**2 > n:
        right = mid -1
    elif mid**2 < n:
        left = mid + 1
    else:
        break
    mid = (left+right)//2

if mid**2 < n:
    print(mid+1)
else:
    print(mid)