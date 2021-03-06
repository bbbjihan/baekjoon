#슬라이딩 윈도우(sliding-window) 알고리즘
import sys;rl=sys.stdin.readline
N,X = map(int,rl().split())
visitant = list(map(int,rl().split()))
ans = 1
preSum = sum(visitant[0:X])
Max = preSum
for i in range(1,N-X+1):
  Sum = preSum - visitant[i-1] + visitant[i+X-1]
  if Sum > Max:
    Max = Sum
    ans = 1
  elif Sum == Max:
    ans+=1
  preSum = Sum

if Max == 0:
  print('SAD')
else:
  print(Max)
  print(ans)