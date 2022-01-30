#다이나믹프로그래밍(DP)
#n을 최대크기로 갖는 리스트를 생성하고, 제곱수를 인덱스로 갖는 원소를 1로 지정,
#순회하며 작은 값부터 최소횟수 갱신
#어떠한 자연수든 4개의 수를 더하여 만들 수 있다는 것은
#그 자연수에서 제곱수를 뺀 수는 3개의 제곱수를 더하여 만들 수 있다는 것을 의미
#또 그 수에서 제곱수를 뺀 수는 2개의 제곱수를 더하여 만들 수 있음.
#따라서 일정한 값보다 작은 임의의 네 개의 제곱수의 합을 구할 수 있다는 말은
#순회하여 그보다 작은 수의 최소 횟수를 구해놓는다면,
#그 최소값들을 활용해 최소값을 도출할 수 있다는 의미.
#https://minhyeok-rithm.tistory.com/entry/BOJ-17626
import math
import sys

N = int(sys.stdin.readline())
dp = [1] * N

for i in range(1,N):
    if i != int(math.sqrt(i)) ** 2: dp[i-1] = i

for i in range(1,N):
    for j in range(int(math.sqrt(i))+1):
        dp[i-1] = min(dp[i-1],dp[j*j]+dp[i-j*j])

print(dp[N])