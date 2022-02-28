selfNumber = [1 for i in range(10001)]
def d(num):
    return sum(list(map(int,str(num))))+num
for i in range(1,10001):
    if selfNumber[i]:
        tmp = d(i)
        while tmp <= 10000:
            selfNumber[tmp] = 0
            tmp = d(tmp)

for i in range(1,10001):
    if selfNumber[i]:
        print(i)