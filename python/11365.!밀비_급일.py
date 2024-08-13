while True:
    l = input().strip()
    if l == 'END':
        break
    print(l[-1:0:-1] + l[0])