import sys

N,K = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))
lPointer = 0
rPointer = 0
M = 0

dic = dict.fromkeys([x for x in range(max(nums) + 1)], 0)

while rPointer < N-1:
    if dic[nums[rPointer]] >= K:
        dic[nums[lPointer]]-=1
        lPointer+=1
    else:
        dic[nums[rPointer]] += 1
        rPointer += 1
    M = max(M, rPointer - lPointer)

print(M)