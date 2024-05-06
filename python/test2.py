import math

N = 11

def getRange(nodeIndex):
  # 1(0~N)
  # 2(0~N/2), 3(N/2 ~ N)
  # 4(0~N/4), 5(N/4,2N/4), 6(2N/4,3N/4), 7(3N/4, N)
  seg = 2 ** int(math.log2(nodeIndex))
  return int((nodeIndex - seg) * (N / seg)), int((nodeIndex - seg + 1) * (N / seg))

for i in range(1,29):
  print(getRange(i))