a = [1,2,3,4,5,6]

def combinations(arr, n):
    result = []
    if n==0:
        return [[]]
    for i in range(len(arr)):
        start = arr[i]
        rest = arr[i+1:]
        for j in combinations(rest,n-1):
            result.append([start]+j)
    return result
        
#print(combinations(a,3))

def permutations(arr, n):
    result = []
    if n ==0:
        return [[]]
    for i in range(len(arr)):
        start = arr[i]
        rest = arr[:i] + arr[i+1:]
        for j in permutations(rest,n-1):
            result.append([start]+j)
    return result
#rint(permutations(a,3))


def combinations1(arr,n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        start = arr[i]
        rest = arr[i+1:]
        for j in combinations(rest,n-1):
            result.append([start]+j)
    return result

#print(combinations1(a,3))

def permutations1(arr,n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        start = arr[i]
        rest = arr[:i] + arr[i+1:]
        for j in permutations1(rest,n-1):
            result.append([start]+j)
    return result
print(permutations1(a,3))




















