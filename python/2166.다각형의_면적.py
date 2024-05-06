#가우스 면적 공식(신발끈 공식) https://ko.wikipedia.org/wiki/%EC%8B%A0%EB%B0%9C%EB%81%88_%EA%B3%B5%EC%8B%9D
import sys;rl=sys.stdin.readline

N = int(rl())
dots = []
for _ in range(N):
  dots.append(list(map(int,rl().split())))

S = 0
for i in range(N - 1):
  S += dots[i][0] * dots[i+1][1] - dots[i+1][0] * dots[i][1]

S += dots[N - 1][0] * dots[0][1] - dots[0][0] * dots[N - 1][1]
print(abs(S / 2))