import math

team = input().strip()

N=int(input())

a = [0,0,0]
for _ in range(N):
    user = input().strip()
    i = user[0]
    for j in range(3):
        a[j] += i == team[j]

x,y,z=team

if len(set(team)) == 3:
    print(a[0] * a[1] * a[2])
elif len(set(team)) == 1:
    print(math.comb(a[0],3))
elif x == y:
    print(math.comb(a[0], 2) * a[2])
elif x == z:
    print(math.comb(a[0], 2) * a[1])
else:
    print(math.comb(a[1], 2) * a[0])