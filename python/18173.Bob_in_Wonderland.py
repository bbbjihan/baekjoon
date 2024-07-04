import sys;rl=sys.stdin.readline
N = int(rl())

links = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, rl().split())
    links[a].append(b)
    links[b].append(a)

cnt_links = [len(link) for link in links]

ans = 0
for cnt in cnt_links:
    if cnt > 2:
        ans += cnt - 2

print(ans)