N=input()

if len(N) == 2:
    print(int(N[0]) + int(N[1]))
    exit()

a,b =[0,0]
for i in range(len(N)):
    if N[i] == '0':
        continue
    if i < len(N)-1 and N[i] == '1' and N[i+1] == '0':
        if a == 0:
            a=10
        else:
            b=10
    else:
        b=int(N[i])
print(a+b)