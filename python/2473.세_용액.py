import sys;rl = sys.stdin.readline

N = int(rl())
liquids = list(map(int, rl().split()))
liquids.sort()

S = 3000000000
ans = [-1, -1, -1]
for i in range(len(liquids)):
    j = i + 1
    k = len(liquids) - 1
    
    while j < k :
        fixed, left, right = liquids[i], liquids[j], liquids[k]
        nowSum = sum([fixed, left, right])
        if S > abs(nowSum):
            S = abs(nowSum)
            ans = [fixed, left, right]
        elif nowSum < 0 :
            j += 1
        else:
            k -= 1
print(*ans)