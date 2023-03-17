n=int(input())
list1 = list(map(int,input().split()))
avg = round(sum(list1)/n)
list2 = list(map(lambda x: avg-x , list1))
list3= []
index1=-1
min = float('inf')
for index, value in enumerate(list2):
    a = 0
    if value < 0:
        value = -value
        a= 1
    if value < min:
        min = value
        index1=index
    elif value == min:
        if a == 0:
            
        