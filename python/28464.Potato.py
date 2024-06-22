import sys;rl=sys.stdin.readline

N = int(rl())
FFs = list(map(int,rl().split()))

FFs.sort(key=lambda x: -x)

start = 0
end = len(FFs)
mid = (start + 1 + end) // 2

print(sum(FFs[mid:end]), sum(FFs[start:mid]))