n = int(input())
for _ in range(n):
    a,u=input().split()
    
    if u == 'kg':
        b=2.2046
        u='lb'
    elif u == 'lb':
        b=0.4536
        u='kg'
    elif u == 'l':
        b=0.2642
        u='g'
    else:
        b=3.7854
        u='l'
    
    print('{:.4f}'.format(float(a) * b)+ ' ' + u)