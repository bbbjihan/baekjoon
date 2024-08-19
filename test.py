import sys;rl=sys.stdin.readline

n,m,q = map(int,rl().split())

teams = [[] for _ in range(n+1)]
# [푼 수, 총 시간, 패널티]

for _ in range(q):
    time, team, quest, result = rl().split()
    time, team, quest = int(time), int(team), int(quest)
    
    