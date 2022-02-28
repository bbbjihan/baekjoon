import sys;rl=sys.stdin.readline

C = int(rl())
for _ in range(C):
    Class = list(map(int,rl().split()))
    Average = sum(Class[1:])/Class[0]
    cntOverMid = 0
    for stu in Class[1:]:
        if stu > Average:
            cntOverMid+=1
    print(str(format((cntOverMid/Class[0])*100,".3f"))+'%')