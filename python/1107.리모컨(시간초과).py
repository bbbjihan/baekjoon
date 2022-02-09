# case1: 100번 채널에서 출발 -> (+),(-)버튼으로 목표값에 도착하는 횟수
# case2: 망가진 버튼들로 목표값을 만들 수 있을 경우 -> 목표값의 자릿수
# case3: 망가진 버튼들로 만든 목표값보다 작은 가장 큰 값 -> 만든 값의 자릿수 + (+),(-)버튼으로 목표값에 도착하는 횟수
# case4: 망가진 버튼들로 만든 목표값보다 큰 가장 작은 값에서 출발 -> 만든 값의 자릿수 + (+),(-)버튼으로 목표값에 도착하는 횟수
# 네 개의 값 중 최솟값을 출력.
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
if M == 0:
    crushed = []
else:
    crushed = sys.stdin.readline().split()
cnt = 0

def can_make(num):
    tmp = set(str(num))
    for a in tmp:
        if a in crushed:
            return False
    return True

def min_case234():
    tmp_3 = tmp_4 = N
    less = 0
    while less == 0:
        if can_make(tmp_3):
            less = 3
            break
        elif can_make(tmp_4):
            less = 4
            break
        tmp_3-=1
        tmp_4+=1
    if less == 3:
        return len(str(tmp_3)) + (abs(N-tmp_3))
    elif less == 4:
        return len(str(tmp_4)) + (abs(N-tmp_4))

if crushed == ['1','2','3','4','5','6','7','8','9']:
    print(min(abs(N-100),N+1))
elif crushed == ['0','1','2','3','4','5','6','7','8','9']:
    print(abs(N-100))
else:
    print(min(abs(N-100),min_case234()))