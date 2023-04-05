n = input()
n = int(n)
a = []
for i in range(n):
    number = input()
    number = int(number)
    a.append(number)

a.sort(reverse = True)
print(a)