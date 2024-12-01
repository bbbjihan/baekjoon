# 백준 27160.할리갈리(https://www.acmicpc.net/problem/27160)

N = int(input())

x = [0] * 4
for _ in range(N):
    a,b = input().split()
    x[0 if a == 'STRAWBERRY' else 1 if a == 'BANANA' else 2 if a == 'LIME' else 3] += int(b)

print('YES' if 5 in x else 'NO')