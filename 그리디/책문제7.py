#solution 1
# n,m = list(map(int, input().split()))
# l = list(map(int, input().split()))
# result = 0
# for i in range(n-1):
#     check = l[i]
#     for j in range(i+1, n):
#         if check != l[j]:
#           result += 1

#solution 2
from collections import Counter
n,m = list(map(int, input().split()))
l = list(map(int,input().split()))
result = 0
a = Counter(l)
b = list(a.keys())
sum = n
for i in range(len(b)-1):
    sum = sum - a[b[i]]
    result = result + sum * a[b[i]]
print(result)

