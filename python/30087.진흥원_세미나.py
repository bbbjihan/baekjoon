import sys;rl=sys.stdin.readline

dict = {
    "Algorithm": "204",
    "DataAnalysis": "207",
    "ArtificialIntelligence": "302",
    "CyberSecurity": "B101",
    "Network": "303",
    "Startup": "501",
    "TestStrategy": "105"
}

N = int(rl())
for _ in range(N):
    print(dict[rl().strip()])