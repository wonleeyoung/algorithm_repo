n,m = list(map(int, input().split()))
l = []
for i in range(n):
    list1 = list(map(int ,input().split()))
    l.append(list1)
list2 =[]
for i in range(n):
    a = min(l[i])
    list2.append(a)
print(max(list2))