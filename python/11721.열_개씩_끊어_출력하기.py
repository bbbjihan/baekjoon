a=list(input().strip())
for i in range(0,len(a)//10):
    print(''.join(a[i*10:i*10+10]))
if len(a)%10 != 0:
    print(''.join(a[len(a)-(len(a) % 10):]))