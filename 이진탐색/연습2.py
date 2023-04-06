def summation(arr, index,n):
    sum = 0
    criteria = arr[index]
    for i in range(index+1,n):
        sum += (arr[i] - criteria)
    return sum

def binary_search(arr,l,h,m):
    first = l
    last = h
    
    while first<=last:
        mid = (first + last)//2
        amount = summation(arr,mid,h+1)
        if amount > m:
            first = mid + 1
        elif amount <m:
            last = mid - 1
        elif amount == m:
            return mid
    return mid
                

n, m = map(int, input().split())
dlist = list(map(int, input().split()))
dlist.sort()

a = binary_search(dlist,0,n-1,m)
sum = summation(dlist,a,n)
h = dlist[a]
if sum == m:
    h = dlist[a]
elif sum>m:
    
    while True:
        check = 0
        h = h + 1
        for i in range(a+1,n):
            if dlist[i] > h:
                check += dlist[i] - h
        if check == m:
            break
        elif check < m:
            h = h - 1
            break
elif sum <m:
    while True:
        check = 0
        h = h - 1
        for i in range(0):
            if dlist[i] > h:
                check += dlist[i] - h
        if check >= m:
            break
print(h)
            