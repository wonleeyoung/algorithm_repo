def solution(tickets):
    answer = ['ICN']
    for_stack = []
    for i in tickets:
        if 'ICN' == i[0]:
            for_stack.append(i)
    for_stack.sort()
    stack = [for_stack[0]]
    tickets.remove(for_stack[0])  # 여기까지는 'icn'만 stack에 넣은 경우임
    
    while len(stack)>0:
        pop_value = stack.pop()
        answer.append(pop_value[1])
        for_stack = []
        for i in tickets:
            if pop_value[1] == i[0]:
                for_stack.append(i) # for_stack 을 만들고 첫번쨰만 꺼낼 예정 
        for_stack.sort()
        stack.append(for_stack[0])
        tickets.remove(for_stack[0])
    return answer
#test case 1번2번 안됨 다시시도해볼예정