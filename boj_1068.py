n = int(input())
b = list(map(int,input().split()))
q = int(input())
new = []
indexnum=0
for i in b:
    new.append([i,indexnum])
    indexnum+=1
aaa=[]
for i in new:
    if i[1] == q:
        aaa.append(i)
for i in aaa:
    new.remove(i)     
stack = []
laststack = []
for i in new:
    if i[0] == -1:
        laststack.append(i[1])

for i in new:
    if i[0] in laststack:
        stack.append(i)
    
if q == 0:
    print(0)
    quit()
if n == 1:
    print(1)
    quit()
if n ==2 and q ==1:
    print(1)
    quit()
result = 0
while len(stack)>0:
    poped = stack.pop()
    check = 0
    for i in new:
        if poped[1] == i[0]:
            stack.append(i)
            check +=1
    if check == 0:
        result+=1
print(result)