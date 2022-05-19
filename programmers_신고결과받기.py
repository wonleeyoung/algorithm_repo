def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    a=set(report)
    report=list(a) # 중복 제거됨
    dict1 = dict()
    
    for i in id_list:
        dict1[i] = []
    for i in report:
        q=i.split()
        dict1[q[1]].append(q[0])
    for i in dict1:
        if len(dict1[i])>=k:
            for j in dict1[i]:
                answer[id_list.index(j)]+=1
    return answer