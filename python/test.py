import sys
n = int(sys.stdin.readline())

tmp = n
power6 = -1
while tmp>=1:
    tmp = tmp/6
    power6+=1

tmp = n - 6 ** power6
power3 = -1
while tmp>=1:
    tmp = tmp/3
    power3+=1

tmp = n - 6 ** power6 - 3 ** power3
power2 = -1
while tmp>=1:
    tmp = tmp/2
    power2+=1

plus1 = n - 6 ** power6 - 3 ** power3 - 2 ** power2

print(power6*2 + power3 + power2 + plus1)