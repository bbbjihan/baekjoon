import sys;rl=sys.stdin.readline

T = int(rl())
for _ in range(T):
    length, count_ant = map(int,rl().split())
    
    longest, shortest = 0, 0
    for _ in range(count_ant):
        left = int(rl())
        right = length - left
        short = min(left, right)
        long = max(left, right)
        
        shortest = max(short, shortest)
        longest = max(long, longest)
    
    print(shortest, longest)