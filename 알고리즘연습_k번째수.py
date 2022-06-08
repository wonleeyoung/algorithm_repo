t=int(input())
for i in range(t):
    n,s,e,k = map(int,input().split())
    list1 = list(map(int,input().split()))
    list1.sort()
    list2 = list1[s-1:e]
    print(list2[k-1])