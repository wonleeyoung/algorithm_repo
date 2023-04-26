def solution(N, number):
    check = [[] for i in range(9)]
    check[1].append(N)
    if number in check[1]:
        return 1
    for i in range(2,9):
        #check[i].append(11*N)
        cc = '1' * i
        cc = int(cc,base = 10)
        check[i].append(cc*N)
        for j in range(1,i):
            first = check[j]
            second = check[i-j]
            for k in first:
                for q in second:
                    check[i].append(k+q)
                    if k+q == number:
                        return i
                    check[i].append(k-q)
                    if k-q == number:
                        return i
                    check[i].append(k*q)
                    if k*q == number:
                        return i
                    if q != 0:
                        check[i].append(k//q)
                        if k//q == number:
                            return i
            check[i] = list(set(check[i]))
        if number in check[i]:
            return i
                
    return -1