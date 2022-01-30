import sys #DP(다이나믹 프로그래밍)
T = int(sys.stdin.readline())
li = []

for i in range(T):
    li.append(int(sys.stdin.readline()))

fi = [0] * (max(li)+1)
fi[1] = 1

for i in range(2,len(fi)):
    fi[i] = fi[i-1] + fi[i-2]
  
for i in li:
    if i == 0:
        print(1,0)
    else:
        print(fi[i-1],fi[i])