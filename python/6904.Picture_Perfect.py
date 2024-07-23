import sys;rl=sys.stdin.readline

def get_min_perimeter(n):
    min_perimeter = n * 2 + 2
    g_a = 1
    g_b = n
    for a in range(1, n + 1):
        if n % a == 0:
            b = n // a
            if 2 * (a + b) < min_perimeter:
                min_perimeter = 2 * (a + b)
                g_a = a
                g_b = b
    return min_perimeter, g_a, g_b

while True:
    n = int(rl())
    if n == 0:
        break
    
    min_param, a, b = get_min_perimeter(n)
    
    print('Minimum perimeter is '+ str(min_param) +' with dimensions '+str(a)+' x '+str(b)+'')