import sys

N,M = map(int,sys.stdin.readline().split())

page = dict()

for i in range(N):
    tmp = sys.stdin.readline().rstrip().split()
    page[tmp[0]] = tmp[1]

for i in range(M):
    tmp = sys.stdin.readline().rstrip()
    print(page[tmp])
