import sys #n을 1과 2로 분할하는 경우의 수를 구하시오. => 피보나치 수열
import math
n = int(sys.stdin.readline())
fib_n = 1
fib_nm1 = 0
for i in range(n):
    tmp = fib_n
    fib_n = fib_nm1+tmp
    fib_nm1 = tmp

print(fib_n%10007)