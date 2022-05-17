from collections import deque
def solution(phone_book):
    answer = True
    list_with_len =[]
    for i in phone_book:
        a=len(i)
        list_with_len.append([i,a])
    list_with_len.sort(key=lambda x : (x[1],x[0]))
    newlist = deque(list_with_len)
    while len(newlist) >1 :
        popque = newlist.popleft()
        for i in range(len(newlist)):
            if popque == newlist[i][0:len(popque)]:
                return False
    return answer
print(solution(["123","456","789"]))