import sys;rl=sys.stdin.readline

T = int(rl())

for _ in range(T):
  N, K = map(int,rl().split())
  time = list(map(int,rl().split()))
  
  indegrees = [ 0 for _ in range(N + 1) ]
  visited = [ False for _ in range(N + 1) ]
  edges = [ [] for _ in range(N + 1) ]
  for _ in range(K):
    start, end = map(int,rl().split())
    indegrees[end] += 1
    edges[start].append(end)
  
  q = []
  dp = [ 0 for _ in range(N + 1) ]
  for i in range(1, N + 1):
    if indegrees[i] == 0:
      q.append(i)
      dp[i] = time[i - 1]
  
  while q:
    now = q.pop(0)
    
    for next in edges[now]:
      indegrees[next] -= 1
      dp[next] = max(dp[next], dp[now] + time[next - 1])
      # max가 쓰이는 이유
      # 어차피 각 노드까지의 시간을 저장할 때는
      # indegree가 0이 됐을 때가 그 노드까지 필요한 테크트리들을 전부 순회했을 땐데,
      # 그 노드를 다음 순서로 가지는 노드들을 순회 중에 모두 마주칠 것이다.
      # 그렇게 마주친 애들이 전부 완료되려면 그 중에서 최대값을 가져가야 함.
      # 그리고 거기서 최대값을 가져간 게 여러 테크를 동시에 진행했어도
      # 올바른 값이 되는 이유는 위상정렬을 통해 앞 순서 노드들부터 순회가 진행되고 있기 때문
      if indegrees[next] == 0:
        q.append(next)
  
  W = int(rl())
  print(dp[W])