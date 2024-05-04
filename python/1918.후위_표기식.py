import sys;rl=sys.stdin.readline

inorder = list(rl().strip())

stack = []

def transfrom(nonBracketExpression, operators):
  stackLoc = []
  i = 0
  while i < len(nonBracketExpression):
    now = nonBracketExpression[i]
    if now in operators:
      prev = stackLoc.pop()
      stackLoc.append(prev + nonBracketExpression[i + 1] + now)
      i += 1
    else:
      stackLoc.append(now)
    i += 1
  
  return stackLoc

for c in inorder:
  if c == ')':
    lastEle = stack.pop()
    inBracket = []
    while lastEle != '(':
      inBracket.append(lastEle)
      lastEle = stack.pop()
    trans1 = transfrom(inBracket[::-1],['*', '/'])
    trans2 = ''.join(transfrom(trans1, ['+', '-']))
    stack.append(trans2)
  else:
    stack.append(c)

trans1 = transfrom(stack,['*', '/'])
trans2 = ''.join(transfrom(trans1, ['+', '-']))
print(''.join(trans2))