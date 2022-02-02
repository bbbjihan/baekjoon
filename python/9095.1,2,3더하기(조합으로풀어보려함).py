import sys
import math

n = int(sys.stdin.readline())
li = []
for i in range(n):
    li.append(int(sys.stdin.readline()))

casecnt = [0 for i in range(max(li)+1)]
combi = [[] for i in range(max(li)+1)]

for i in range(1,max(li)+1):
    cnt1, cnt2, cnt3 = i, 0, 0
    
    while cnt3*3<=i:
        cnt1=i-cnt3*3
        cnt2=0
        combi[i].append([cnt1,cnt2,cnt3])
        while cnt1>1:
            cnt2+=1
            cnt1-=2
            combi[i].append([cnt1,cnt2,cnt3])
        cnt3+=1

for i in range(1,max(li)+1):
    cnt = 0
    for j in combi[i]:
        cnt+= math.factorial(j[0]+j[1]+j[2])/math.factorial(j[0])*math.factorial(j[1])*math.factorial(j[2])
    casecnt[i] = cnt
        

print(combi)
print(casecnt)
for i in li:
    print(casecnt[i])