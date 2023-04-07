#n = int(input())

def gen_combinations(arr, n):
    result =[] 

    if n == 0: 
        return [[]]

    for i in range(0, len(arr)): 
        elem = arr[i] 
        rest_arr = arr[i + 1:] 
        for C in gen_combinations(rest_arr, n-1): 
            result.append([elem]+C) 
              
    return result
def gen_permutations(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i, elem in enumerate(arr): 
        for P in gen_permutations(arr[:i] + arr[i+1:], n-1):
            result += [[elem]+P]
              
    return result
    
    

                

def combinations(arr, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        index = arr[i]
        rest  = arr[i+1:]
        for j in combinations(rest,n-1):
            result.append([index]+j)
    return result

print(combinations([1,2,3],2))




def combination(arr, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        first = arr[i]
        rest = arr[i+1:]
        for j in combination(rest,n-1):
            result.append([first]+j)
    return result

def permutation(arr, n):
    result = []
    
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        index = arr[i]
        rest = arr
        for j in permutation(rest,n-1):
            result.append([index]+j)
    return result
print(permutation([1,2,3],2))