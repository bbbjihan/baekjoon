kangs = list(map(int,input().split()))
kangs.sort()

ans = max(kangs[1] - kangs[0], kangs[2] - kangs[1])

print(ans - 1)