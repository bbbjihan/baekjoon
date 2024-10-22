m = {
    'A':'B', 
    'B':'C', 
    'C':'D', 
    'D':'E', 
    'E':'F', 
    'F':'G', 
    'G':'H', 
    'H':'I', 
    'I':'J', 
    'J':'K', 
    'K':'L', 
    'L':'M', 
    'M':'N', 
    'N':'O', 
    'O':'P', 
    'P':'Q', 
    'Q':'R', 
    'R':'S', 
    'S':'T', 
    'T':'U', 
    'U':'V', 
    'V':'W', 
    'W':'X', 
    'X':'Y', 
    'Y':'Z', 
    'Z':'A'
}
N = int(input())
for i in range(1, N+1):
    l=''.join(list(map(lambda x:m[x], input().strip())))
    print('String #' + str(i))
    print(l)
    print('')