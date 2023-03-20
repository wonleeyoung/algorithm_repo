n = int(input())
a = list(map(int,input().split()))
a.sort()
count = 0
v = 1
for i in range(len(a)):
    if a[i] == v:
        count += 1
        v = 1
    else:
        v += 1

print(count)