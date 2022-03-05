import sys;rl=sys.stdin.readline

li = [True for _ in range(246913)]
primeNum = []
li[0], li[1] = False, False
for i in range(2,246913):
    if li[i]:
        j = i*2
        while j<len(li):
            li[j] = False
            j+=i
for i in range(246913):
    if li[i]:
        primeNum.append(i)

def binarySearch(num):
    left = 0
    right = len(primeNum)-1
    while left <= right:
        mid = (left+right)//2
        if primeNum[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    return left
                
while 1:
    case = int(rl())
    if not case:
        break
    print(binarySearch(case*2)-binarySearch(case))