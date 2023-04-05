n = input()
n = int(n)

a=  []
for i in range(n):
    name, score = input().split()
    score = int(score)
    data = [name, score]
    a.append(data)

def score(data):
    return data[1]

new = sorted(a, key = score)
print(new)