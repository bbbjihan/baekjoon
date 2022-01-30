#최소개수가 1인 경우는 n의 제곱근이 정수인 경우
#최소개수가 2인 경우는 임의의 정수 i에 대하여 n-i^2의 제곱근이 정수인 경우
#최소개수가 3인 경우는 임의의 정수 i,j에 대하여 n-i^2-j^2의 제곱근이 정수인 경우
#else 최소개수 4

import sys
N = int(sys.stdin.readline().rstrip())

def is_sqr(num):
    if num**0.5 == int(num**0.5):
        return True
    else:
        return False

def get_min(num):
    if is_sqr(num):
        return 1
    else:
        for i in range(1,int(num**0.5)+1):
            if is_sqr(num-i**2):
                return 2

        for i in range(1,int(num**0.5)+1):
            for j in range(1,int((num-i**2)**0.5)+1):
                if is_sqr(num-i**2-j**2):
                    return 3
    return 4

print(get_min(N))