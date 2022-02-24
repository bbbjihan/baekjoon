import sys;rl=sys.stdin.readline

a = [2,4,6,8,10,12,14,16,18,20]
b = [1,2,3,4,5,6,12,20,18]

for target in b:
    left = 0
    right = len(a)-1
    mid = (left+right)//2
    while left < right:
        if a[mid] > target:
            right = mid - 1
        elif a[mid] < target:
            left = mid + 1
        else:
            break
        mid = (left+right)//2
    print(mid)