a = int(input())
b = int(input())
c = int(input())

if a + b + c == 180:
    if a == b or a == c or b == c:
        if a == b == c:
            print("Equilateral")
        else:
            print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")