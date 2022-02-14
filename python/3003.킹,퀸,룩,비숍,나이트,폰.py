pieces = list(map(int,input().split()))
case = [1,1,2,2,2,8]
for i in range(6):
  case[i] = str(case[i]-pieces[i])
print(' '.join(case))