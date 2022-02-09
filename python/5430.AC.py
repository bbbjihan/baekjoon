import sys

N = int(sys.stdin.readline())

for _ in range(N):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    tmp = sys.stdin.readline().rstrip()
    if tmp == '[]':
        li = []
    else:
        li = list(map(int,tmp[1:len(tmp)-1].split(',')))
    flag = 0 #정방향의 경우 0, 역방향의 경우 1
    left_idx = 0
    right_idx = n-1
    error_flag = 0

    for com in p:
        length = right_idx - left_idx + 1
        if com == 'R':
            if flag == 0:
                flag = 1
            else:
                flag = 0
        else:
            if length == 0:
                error_flag = 1
                break
            else:
                if flag == 0:
                    left_idx+=1
                else:
                    right_idx-=1
    if error_flag == 1:
        print('error')
    elif flag == 0:
        tmp = list(map(str,li[left_idx:right_idx+1]))
        print('['+','.join(tmp)+']')
    else:
        tmp = list(map(str,li[right_idx-n:left_idx-n-1:-1]))
        print('['+','.join(tmp)+']')