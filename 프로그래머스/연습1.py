def solution(numbers):
    answer = ''
    l = []
    for i in numbers:
        l1 = []
        if i // 1000 != 0:
            l1.append(i//1000)
            l1.append(i) 
            l.append(l1)
            continue
    
        if i // 100 != 0:
            l1.append(i//100)
            l1.append(i)
            l.append(l1)
            continue
        
        if i // 10 != 0:
            l1.append(i//10)
            l1.append(i)
            l.append(l1)
            continue
        l1.append(i)
        l1.append(i)
        l.append(l1)
    
    a = sorted(l,reverse=True)    
    return a

print(solution([1,2,3,34,51]))