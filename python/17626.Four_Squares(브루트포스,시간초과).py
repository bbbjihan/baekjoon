import sys
import math

N = int(sys.stdin.readline().rstrip())
breaker = 0

def get_less_square(num): #n보다 작거나 같은 수 중 가장 큰 제곱수를 구함
    if num <= 0:
        num = 1
    for i in range(int(num),0,-1):
        x = math.sqrt(i)
        if x == int(x):
            return i

#그리디로 풀되, 크기순으로 첫번째 제곱수를 줄여가면서 구함.
#첫번째 제곱수가 줄어들다가 두번째 제곱수보다 작아지는 순간 while문 탈출
#만들어진 answer 배열에서 최소값 출력

#아니다... 1개로 만들 수 있는지부터 확인.
#그리고 2개로 만들 수 있는지 확인
#3개로 만들 수 있는지 확인, 안되면 4 출력하는 식으로 해야겠다. 이게 더 빠를 거 같은데?

N1 = get_less_square(N)
if N == N1:
    print(1)
    breaker = 1

if breaker != 1:
    N2 = get_less_square(N-N1)
    while N1>=N2:
        if N1+N2 == N:
            print(2)
            breaker = 2
            break
        else:
            N1 = get_less_square(N1-1)
            N2 = get_less_square(N-N1)
    
    if breaker != 2:
        N1 = get_less_square(N)
        N2 = get_less_square(N-N1)
        N3 = get_less_square(N-N1-N2)
        while N1>=N2:
            while N2>=N3:
                if N1 + N2 + N3 == N:
                    print(3)
                    breaker = 3
                    break
                else:
                    N2 = get_less_square(N2-1)
                    N3 = get_less_square(N-N1-N2)
            if breaker == 3:
                break
            else:
                N1 = get_less_square(N1-1)
                N2 = get_less_square(N-N1)
                N3 = get_less_square(N-N1-N2)
                


if breaker == 0:
    print(4)