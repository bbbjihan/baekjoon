import sys;rl=sys.stdin.readline

N = int(rl())

board = []

def get_time_str(time):
    min = time // 60
    sec = time % 60
    return ('0' if min < 10 else '') + str(min) + ':' + ('0' if sec < 10 else '') + str(sec)

for _ in range(N):
    team, time = rl().split()
    min = int(time[:2])
    sec = int(time[-2:])
    
    time = min * 60 + sec
    
    board.append((time, int(team)))

board.append((0, 0))
board.append((48 * 60, 0))
board.sort(key=lambda x:x[1])
board.sort(key=lambda x:x[0])
t1, t2, s1, s2 = 0, 0, 0, 0
prev_winning = 0

for i in range(1, N + 2):
    time, team = board[i]
    prev_time, _ = board[i-1]
    time_diff = time - prev_time
    
    if prev_winning == 1:
        t1 += time_diff
    elif prev_winning == 2:
        t2 += time_diff
    
    if team == 1:
        s1 += 1
    elif team == 2:
        s2 += 1
    
    if s1 > s2:
        prev_winning = 1
    elif s1 < s2:
        prev_winning = 2
    else:
        prev_winning = 0

print(get_time_str(t1))
print(get_time_str(t2))