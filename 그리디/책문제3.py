n,k = list(map(int,input().split()))
count  = 0
while n != 1:
    a = n % k
    if a == 0:
        n = n//k
        count += 1
    else:
        n = n - a
        count += a
print(count)