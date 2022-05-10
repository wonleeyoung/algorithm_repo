dict1 = {}
count = 1
for i in range(97,123):
    dict1[chr(i)] = count
    count+=1
l = int(input())
string = input()
a = 0
sum = 0
for i in string:
    sum = sum + dict1[i]*(31**a)
    a+=1
print(sum%1234567891)