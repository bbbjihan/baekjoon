m, d = map(int,input().split())

md = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
wd = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

days = sum(md[0:m]) + d 
print(wd[days % 7])