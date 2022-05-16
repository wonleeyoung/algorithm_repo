def solution(p):
    if p =='':  # 주어진 문자열이 빈 문자열일 경우 빈 문자열을 반환합니다.
        return ''
    # 첫번째 문자열을 균형잡힌 문자열로 분리시킨다. - 더이상 쪼갤 수 없는 상태 
    left_num = 0 
    right_num =0
    index_num = 0
    for i in range(len(p)):
        if p[i] == '(':
            left_num+=1
        elif p[i] ==')':
            right_num+=1
        if left_num == right_num: # 첫번째 균형잡힌 문자열이 만들어 질때까지 시행한다는 뜻
            index_num = i
            break
        index_num = i    
    # u와 v의 문자열 부여
    if index_num+1 == len(p):
        u = p[:]
        v = ''
    else:
        u =p[:i+1]
        v =p[i+1:]
    # 더이상 분리할 수 없는 + 균형잡힌 문자열은 첫 시작이 ( 라면 무조건 올바른 괄호 문자열이다. 
    if u[0] == '(':
        return u + solution(v) # 문제의 3번 case
    else: # 문제의 4번 케이스 
        string1 = ''
        for i in u[1:len(u)-1]:
            if i == '(':
                i =')'
            elif i==')':
                i='('
            string1+=i # string1은 문제에서 4-4에 해당
        newstring = '(' + solution(v) + ')' + string1 # 최종 결과물
        return newstring
        
    