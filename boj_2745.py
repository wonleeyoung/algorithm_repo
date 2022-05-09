n,b = input().split()
a=[str(i) for i in range(0,10)]
c=[chr(i) for i in range(65,91)]
list1=a+c
number = [i for i in range(0,36)]
index_num = 0
value = 0
for i in range(len(n),0,-1):
    value+=number[list1.index(n[index_num])] * (int(b)**(i-1))
    index_num+=1
print(value)