import sys
N, M = map(int,sys.stdin.readline().split())
num = 0
List = []
Dict = dict()

for i in range(N):
    name = sys.stdin.readline().rstrip()
    num+=1
    Dict[name] = num
    List.append(name)

for i in range(M):
    command = sys.stdin.readline().rstrip()
    if command.isnumeric():
        print(List[int(command)-1])
    else:
        print(Dict[command])
