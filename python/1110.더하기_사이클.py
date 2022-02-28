original=input().rstrip()#STRING
cntCycle=1

NewOrigin = original
if len(NewOrigin) == 1:
    tmp = NewOrigin+'0'
else:
    tmp = NewOrigin
tmp2 = str(int(tmp[0])+int(tmp[1]))
NewOrigin = NewOrigin[len(NewOrigin)-1]+tmp2[len(tmp2)-1]

while int(original) != int(NewOrigin):
    if len(NewOrigin) == 1:
        tmp = NewOrigin+'0'
    else:
        tmp = NewOrigin
    tmp2 = str(int(tmp[0])+int(tmp[1]))
    if NewOrigin[len(NewOrigin)-1] == 0:
        NewOrigin = tmp2[len(tmp2)-1]
    else:
        NewOrigin = NewOrigin[len(NewOrigin)-1]+tmp2[len(tmp2)-1]
    cntCycle+=1

print(cntCycle)