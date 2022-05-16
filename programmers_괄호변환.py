def solution(p):
    answer = ''
    if p =='':
        return ''
    left_num = 0
    right_num =0
    index_num = 0
    for i in range(len(p)):
        if p[i] == '(':
            left_num+=1
        elif p[i] ==')':
            right_num+=1
        if left_num == right_num:
            index_num = i
            break
        index_num = i    
    if index_num+1 == len(p):
        u = p[:]
        v = ''
    else:
        u =p[:i+1]
        v =p[i+1:]
        
    if u[0] == '(':
        return u + solution(v)
    else:
        string1 = ''
        for i in u[1:len(u)-1]:
            if i == '(':
                i =')'
            elif i==')':
                i='('
            string1+=i
        newstring = '(' + solution(v) + ')' + string1
        return newstring
        
    return answer