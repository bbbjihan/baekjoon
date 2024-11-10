ha, ma, sa=map(int,input().split(':'))
hb, mb, sb=map(int,input().split(':'))

a=((ha*60+ma)*60)+sa
b=((hb*60+mb)*60)+sb

if a >= b:
    b += 24 * 60 * 60

c = b-a
ch = c//3600
cm = (c - ch * 3600) // 60
cs = c % 60
print(':'.join([str(ch).zfill(2),str(cm).zfill(2),str(cs).zfill(2)]))