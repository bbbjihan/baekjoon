import sys;rl=sys.stdin.readline
def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    if num == 2:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(int(rl())))