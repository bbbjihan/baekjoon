import sys;rl=sys.stdin.readline

sudoku = []

for _ in range(9):
  sudoku.append(list(map(int,list(rl().strip()))))

def printMat(matrix):
  for i in range(len(matrix)):
    print(''.join(list(map(str,matrix[i]))))

def promising(row,col,num):
  if num in sudoku[row]:
    return False
  for line in sudoku:
    if num == line[col]:
      return False
  start_col = (col//3)*3
  start_row = (row//3)*3
  for square_line in range(start_row,start_row+3):
    if num in sudoku[square_line][start_col:start_col+3]:
      return False
  return True

blinks = []
for i in range(9):
  for j in range(9):
    if sudoku[i][j] == 0:
      blinks.append((i,j))

def dfs(blinkPointer):
  if blinkPointer == len(blinks):
    printMat(sudoku)
    exit()
  blinkY, blinkX = blinks[blinkPointer]
  for i in range(1,10):
    if promising(blinkY, blinkX,i):
      sudoku[blinkY][blinkX] = i
      dfs(blinkPointer+1)
      sudoku[blinkY][blinkX] = 0

dfs(0)