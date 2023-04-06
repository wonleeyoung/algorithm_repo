x = int(input())
# 1빼기, 2나누기, 3나누기 5나누기

arr = [0 for i in range(30001)]
arr[0] = 0
arr[1] = 0

for i in range(2,x+1):
    a = 30000
    b = 30000
    c = 30000
    d = 30000
    if i%2 == 0:
        a = arr[i//2]
    if i%3 == 0:
        b = arr[i//3]
    if i%5 == 0:
        c = arr[i//5]
    d = arr[i-1]
    arr[i] = min(a,b,c,d)+1
print(arr[x])
        