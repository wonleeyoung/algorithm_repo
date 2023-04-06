def binary_search(item, search,l,h):
    start = l
    end = h
    while(start<=end):
        mid = (start+end)//2
        if item[mid] == search:
            return True
        elif item[mid] > search:
            end = mid -1
        elif item[mid] < search:
            start = mid + 1
    return False
    


n = int(input())
item = list(map(int, input().split()))
m = int(input())
search_item = list(map(int, input().split()))

item.sort()
for i in search_item:
    print(binary_search(item, i, 0, n-1),end = ' ')

