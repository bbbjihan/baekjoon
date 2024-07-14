hour, minute, second = map(int,input().split())
timeDiff = int(input())

hourDiff = timeDiff // 3600
timeDiff -= hourDiff * 3600
minuteDiff = timeDiff // 60
timeDiff -= minuteDiff * 60

second += timeDiff
if second >= 60:
    second -= 60
    minute += 1

minute += minuteDiff
if minute >= 60:
    minute -= 60
    hour += 1

hour += hourDiff
hour = hour % 24

print(hour,minute,second)