def solution(board, moves):
    answer = 0
    list1 = []
    for i in range(len(moves)):
        moves[i] = moves[i] - 1
    for i in moves:
        for j in range(len(board)):
            if board[j][i] != 0:
                list1.append(board[j][i])    
                board[j][i] = 0
                break
        if len(list1) > 1 and list1[-1] == list1[-2]:
            answer = answer + 2
            list1.pop()
            list1.pop()
    return answer