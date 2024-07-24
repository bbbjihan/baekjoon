import sys;rl=sys.stdin.readline

while True:
    name, age, weight = rl().split()
    if name == '#':
        break
    age, weight = int(age), int(weight)
    
    print(name, 'Senior' if age > 17 or weight >= 80 else 'Junior')