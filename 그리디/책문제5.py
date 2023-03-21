a = input()
l = [int(i) for i in a]

current = l[0]
count0 = 0
count1 = 0
length = len(l)
for i in range(1,length):
    if l[i] == l[i-1]:
        if i == length-1:
            if l[i] == 0:
                count0 += 1
            else:
                count1 += 1
    else:
        if l[i-1] == 0:
            count0 += 1
            if i == length - 1:
                count1 += 1
        elif l[i-1] == 1:
            count1 += 1
            if i == length - 1:
                count0 += 1
print(min(count0, count1))
        
    
        
