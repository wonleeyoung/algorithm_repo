n = int(input())

l = [0 for i in range(n+1)]

l[1]=1
l[2]=3
for i in range(3,n+1):
    l[i] = 2*l[i-2] + l[i-1]
print(l[n]%796796)