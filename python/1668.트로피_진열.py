import sys;rl=sys.stdin.readline

n = int(rl())
ts = [int(rl()) for _ in range(n)]

left_view = [-1] * 101
right_view = [-1] * 101

for right_index in range(n):
    left_index = n - right_index - 1
    
    right_now = ts[right_index]
    right_view[:right_now] = [right_index] * right_now
    
    left_now = ts[left_index]
    left_view[:left_now] = [left_index] * left_now

print(len(set(left_view)) - 1)
print(len(set(right_view)) - 1)