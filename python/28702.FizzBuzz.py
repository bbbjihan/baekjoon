import sys;rl=sys.stdin.readline

a = rl().strip()
b = rl().strip()
c = rl().strip()

def fizzbuzz(num):
    isFizz = num % 3 == 0
    isBuzz = num % 5 == 0
    if isFizz and isBuzz:
        return 'FizzBuzz'
    elif isFizz:
        return 'Fizz'
    elif isBuzz:
        return 'Buzz'
    else:
        return num

num = int(a) + 3 if a.isdecimal() else int(b) + 2 if b.isdecimal() else int(c) + 1
print(fizzbuzz(num))