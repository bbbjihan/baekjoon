t=int(input())
for _ in range(t):
    input()
    n=int(input())
    a=0
    for _ in range(n):
        a+=int(input())
    print('YES' if a%n== 0 else 'NO')