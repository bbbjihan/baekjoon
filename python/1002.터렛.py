import sys;rl=sys.stdin.readline

def dis(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    return (dx**2+dy**2)**(1/2)

N = int(rl())

for _ in range(N):
    x1,y1,r1,x2,y2,r2 = map(int,rl().split())
    #큰 원을 O1으로 고정
    if r1<r2:
        x1,y1,r1,x2,y2,r2 = x2,y2,r2,x1,y1,r1
    
    disO = dis(x1,y1,x2,y2)
    #두 원의 중점이 같은 경우
    if x1==x2 and y1==y2:
        #두 원의 반지름도 같은 경우 -> 무수히 많은 점에서 만남
        if r1==r2:
            print(-1)
        #두 원의 반지름은 다른 경우 -> 만나지 않음
        else:
            print(0)
    #두 원의 중점이 다른 경우
    #작은 원이 큰 원 안에 있는 경우
    elif r1 > disO:
        #반지름의 차보다 중점사이의 거리가 가까운 경우 -> 만나지 않음
        if (r1-r2)>disO:
            print(0)
        #반지름의 차보다 중점사이의 거리가 먼 경우 -> 두 점에서 만남
        elif (r1-r2)<disO:
            print(2)
        #반지름의 차와 중점사이의 거리가 같은 경우 -> 한 점에서 만남
        else:
            print(1)
    #작은 원이 큰 원 위에 있는 경우 -> 두 점에서 만남(r>0)
    elif r1 == disO:
        print(2)
    #작은 원이 큰 원 밖에 있는 경우
    else:
        #반지름의 합보다 중점 사이의 거리가 큰 경우 -> 만나지 않음
        if (r1+r2)<disO:
            print(0)
        #반지름의 합보다 중점 사이의 거리가 작은 경우 -> 두 점에서 만남
        elif (r1+r2)>disO:
            print(2)
        #반지름의 합과 중점 사이의 거리가 같은 경우 -> 한 점에서 만남
        else:
            print(1)