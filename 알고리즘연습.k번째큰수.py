n,q = map(int,input().split())
list1 = list(map(int,input().split()))
list2 = []
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            a = list1[i]+list1[j]+list1[k]
            list2.append(a)
list2 = set(list2)
list2 = list(list2)
list2.sort()
print(list2[-q])
# for문에 있는 변수도 결국 저장되는것임