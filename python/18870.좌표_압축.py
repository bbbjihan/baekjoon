import sys

N = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
li_dic = list(set(li))
li_dic.sort()
dic = {li_dic[i]:i for i in range(len(li_dic))}
for i in range(N):
    li[i] = str(dic[li[i]])

print(' '.join(li))