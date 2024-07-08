N = int(input())

print(sum(range(1, N+1)))
print(sum(range(1, N+1)) ** 2)
print(sum(list(map(lambda x: x ** 3, range(1, N + 1)))))