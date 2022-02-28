now = list(map(int,input().split()))
plusM = int(input())
now[1]+=plusM
while now[1]>=60:
    now[1]-=60
    now[0]+=1
while now[0]>=24:
    now[0]-=24
print(now[0],now[1])