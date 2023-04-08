n = int(input())
player = []
for i in range(n):
    player.append(list(map(int, input().split())))

def combinations(arr,n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        index = arr[i]
        rest = arr[i+1:]
        for j in combinations(rest,n-1):
            result.append([index]+j)
    return result

def permutation(arr,n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        index = arr[i]
        rest = arr[0:i] + arr[i+1:]
        for j in permutation(rest,n-1):
            result.append([index]+j)
    return result
    
    

div = n/2

opposite = []
comb = combinations([i for i in range(n)],div)
for i in comb:
    opposite1 = []
    for j in range(n):
        if j not in i:
            opposite1.append(j)
    opposite.append(opposite1)
# comb and oppostite 각각 선수들 모음 
sum1 = []
sum2 = []
for i in range(len(comb)):
    sum = 0
    for j in permutation(comb[i],2):
        sum += player[j[0]][j[1]]
    sum1.append(sum)
    
for i in range(len(opposite)):
    sum = 0
    for j in permutation(opposite[i],2):
        sum += player[j[0]][j[1]]
    sum2.append(sum)
    
diff = []
for i in range(len(comb)):
    if sum1[i] >= sum2[i]:
        result = sum1[i] - sum2[i]
    else:
        result = sum2[i] - sum1[i]
    diff.append(result)
print(min(diff))