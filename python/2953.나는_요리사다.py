winner = 0
score = 0
for i in range(5):
    s = list(map(int,input().split()))
    if sum(s) > score:
        winner = i + 1
        score = sum(s)
print(winner, score)