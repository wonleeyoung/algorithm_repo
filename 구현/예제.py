nn = int(input())
l = input().split()
n , m = (1,1)
for i in range(len(l)):
    if l[i] == 'R':
        if m<nn: m+=1
    elif l[i] == 'L':
        if m>1: m-=1
    elif l[i] == "U":
        if n>1 : n-=1
    elif l[i] == "D":
        if n<nn: n+=1
print(n,m)
