import sys;rl=sys.stdin.readline

T, N = map(int,rl().split())

playerData = [{"place": 1, "inventory" : [0 for _ in range(54)]} for _ in range(N + 1)]
logs = []
blocks = set()

for _ in range(T):
    no, player, code, *args = rl().split()
    no, player, args = int(no), int(player), list(map(int,args))
    
    if code == 'M':
        playerData[player]["place"] = args[0]
    elif code == 'F':
        if playerData[player]["place"] != args[0]:
            logs.append(no)
        playerData[player]["inventory"][args[0]] += 1
    elif code == 'C':
        if playerData[player]["inventory"][args[0]] == 0 or playerData[player]["inventory"][args[1]] == 0:
            logs.append(no)
        playerData[player]["inventory"][args[0]] = playerData[player]["inventory"][args[0]] - 1 if playerData[player]["inventory"][args[0]] > 0 else 0
        playerData[player]["inventory"][args[1]] = playerData[player]["inventory"][args[1]] - 1 if playerData[player]["inventory"][args[1]] > 0 else 0
    else:
        if playerData[player]["place"] != playerData[args[0]]["place"]:
            logs.append(no)
            blocks.add(player)

print(len(logs))
if len(logs) > 0:
    print(*logs)
blocks = list(blocks)
blocks.sort()
print(len(blocks))
if len(blocks) > 0:
    print(*blocks)