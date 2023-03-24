a = input()
x = a[0]
y = a[1]
count = 0
# jump 2 first - left right
if x != 'a' and x != 'b':
    if y != '1': count+=1
    if y != '8': count+=1
if x != 'g' and x != 'h':
    if y != '1': count+=1
    if y != '8': count+=1
# jump 2 first - up down
if y != '1' and y != '2':
    if x != 'a': count+=1
    if x != 'h': count+=1
if y != '7' and y != '8':
    if x != 'a': count+=1
    if x != 'h': count+=1
print(count)

## 이동할 수 있는 경로를 리스트에 담아두는 방법을 생각해내자! 
## a = [[1,2],[2,1].....]