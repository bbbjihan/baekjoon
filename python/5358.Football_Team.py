import sys;rl=sys.stdin.read

def translate(S:str):
    new_S = ''
    for i in range(len(S)):
        char = S[i]
        if char == 'i':
            new_S += 'e'
        elif char == 'e':
            new_S += 'i'
        elif char == 'I':
            new_S += 'E'
        elif char == 'E':
            new_S += 'I'
        else:
            new_S += char
    return new_S

inputs = rl().split('\n')

for input in inputs:
    print(translate(input))