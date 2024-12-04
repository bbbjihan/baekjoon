while True:
    A, B = input().split()
    if A == '0' and B == '0':
        break
    maxLen = max(len(A), len(B))
    
    carry = 0
    ans = 0
    for a,b in zip(A.zfill(maxLen)[::-1], B.zfill(maxLen)[::-1]):
        s = int(a) + int(b) + carry
        if s >= 10:
            carry = 1
            ans += 1
        else:
            carry = 0
    print(ans)