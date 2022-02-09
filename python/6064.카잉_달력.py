import sys

calendar = []
N = int(sys.stdin.readline())
for _ in range(N):
    calendar.append(list(map(int,sys.stdin.readline().split())))

def sol(m,n,x,y): #최대가 <m:n>인 카잉 달력에서 <x:y>가 몇번째 해인지 리턴하는 함수
    while x <= m * n:
        if (x-y)%n == 0:
            return x
        x+=m
    return -1

for i in calendar:
    print(sol(i[0],i[1],i[2],i[3]))