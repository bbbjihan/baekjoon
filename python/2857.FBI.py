a = []
for i in range(1,6):
    if 'FBI' in input().strip():
        a.append(str(i))
print(' '.join(a) if len(a) > 0 else 'HE GOT AWAY!')
