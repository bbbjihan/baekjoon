def sol():
    h1,m1,s1,h2,m2,s2 = map(int,input().split())
    t1 = h1 * 3600 + m1 * 60 + s1
    t2 = h2 * 3600 + m2 * 60 + s2
    diff = t2-t1
    h3 = diff // 3600
    m3 = (diff - (h3 * 3600)) // 60
    s3 = diff % 60
    print(h3,m3,s3)

sol()
sol()
sol()