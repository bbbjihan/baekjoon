from math import log2
import sys;rl=sys.stdin.readline

#수열의 시작과 끝을 전달하면 최솟값의 인덱스를 반환하는 함수
def getMinIndex(start,end):
    global An
    if start<=end:
        return An[start:end+1].index(min(An[start:end+1]))+start
    return False

#탑다운 방식을 위해서 전역변수로 트리를 선언하고, 트리의 루트노드부터 리프노드까지 값을 채워나감
#트리의 각 노드는 [구간 내 최소값의 An에서의 인덱스,구간시작,구간끝]형태로 저장됨.
def init():
    global leafLevel,ST,An
    N = An[0]
    minIndex = getMinIndex(1,N)
    ST[0], ST[1] = None, [minIndex,1,N]
    level = 1
    while level <= leafLevel:
        for nodeIndex in range(2**(level-1),2**level,2):
            if ST[nodeIndex//2]:
                parentNodeValue,parentNodeStart,parentNodeEnd = ST[nodeIndex//2]
                if parentNodeValue > 0 and getMinIndex(parentNodeStart,parentNodeValue-1):
                    ST[nodeIndex] = [getMinIndex(parentNodeStart,parentNodeValue-1),parentNodeStart,parentNodeValue-1]
                if parentNodeValue < N and getMinIndex(parentNodeValue+1,parentNodeEnd):
                    ST[nodeIndex+1] = [getMinIndex(parentNodeValue+1,parentNodeEnd),parentNodeValue+1,parentNodeEnd]
        level+=1

def query():
    global ST
    Max = 0
    for node in ST:
        if node == None:
            continue
        Max = max((node[2]-node[1]+1)*An[node[0]],Max)
    return Max

while 1:
    inp = rl().rstrip()
    if inp == '0':
        break
    An = list(map(int,inp.split()))
    #각 직사각형의 높이값을 의미하는 배열이 입력, An[0]은 직사각형의 갯수
    leafLevel = int(log2(An[0]))+2
    ST = [None for _ in range(2**leafLevel)]
    init()
    print(query())