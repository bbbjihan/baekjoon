import sys
n = int(sys.stdin.readline())
li = []
for i in range(n):
    li.append(int(sys.stdin.readline()))

casecnt = [0 for i in range(max(li)+1)]
casecnt[1],casecnt[2],casecnt[3] = [1,2,3]

print(casecnt)