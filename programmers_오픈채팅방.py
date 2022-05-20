def solution(record):
    answer = []
    list1 = []
    for i in record:
        list1.append(i.split())
    dict1 = dict()
    for i in list1:
        if i[0] != 'Leave':
            dict1[i[1]]=i[2]
    for i in list1:
        if i[0] == 'Enter':
            answer.append(dict1[i[1]]+'님이 들어왔습니다.')
        elif i[0] == 'Leave':
            answer.append(dict1[i[1]]+'님이 나갔습니다.')
        
    return answer