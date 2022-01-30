import sys
from collections import Counter

string = list(sys.stdin.readline().rstrip())

#print(string)
pointer = 0
length = 0
cnt = Counter(string)
tmp_len = 0

while cnt['(']!=0:
    if string[pointer] == ')':
        tmp_ptr = pointer
        while string[tmp_ptr] != '(':
            tmp_ptr-=1
        tmp_len = (pointer-tmp_ptr-1+tmp_len)*int(string[tmp_ptr-1])
        del string[tmp_ptr-1:pointer+1]    
        pointer = tmp_ptr-2
        #print(tmp_len)
    elif string[pointer] == '(':
        length += tmp_len
        tmp_len = 0
    pointer+=1
    cnt = Counter(string)

length += len(string) + tmp_len
print(length)