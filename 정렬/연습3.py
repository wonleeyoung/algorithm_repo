n,k = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k):
    if a[i] > b[i]:
        break
    a[i] = b[i]    

print(sum(a))
    