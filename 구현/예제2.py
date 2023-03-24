n = int(input())
hour = 0
minute = 0
second = 0
count = 0
while True:
    second += 1
    if second == 60:
        second = 0
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1
    
    checks = second % 10
    checks1 = second // 10
    checkm = minute % 10
    checkm1 = minute // 10
    checkh = hour % 10
    if (checks == 3) or (checks1 == 3) or (checkm == 3) or (checkm1 == 3) or (checkh == 3): 
        count += 1
    if (hour == n) and (minute == 59) and (second == 59): break;
print(count)