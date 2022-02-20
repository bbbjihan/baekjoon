import sys #재귀 함수 처리순서 진짜 어렵다...
sys.setrecursionlimit(10000000)
preorder = []

while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break

def getPO(start,end):
    if start > end:
        return
    mid = end + 1
    for i in range(start+1,end+1):
        if preorder[start] < preorder[i]:
            mid = i
            break
    getPO(start+1,mid-1)
    getPO(mid,end)
    print(preorder[start])

getPO(0,len(preorder)-1)