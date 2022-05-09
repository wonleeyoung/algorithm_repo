def solution(n, arr1, arr2):
    answer = []
    list1 = []
    list2 = []
    answer1=''
    answer2= []
    for i in arr1: # arr1의 그림을 리스트로 표현하기 위한 과정입니다
        i=bin(i)
        a= '0'*(n+2-len(i)) + i[2:] #2진법으로 변환하고 길이를 n으로 맞췄습니다
        list1.append(a)
    for i in arr2: # 위와 마찬가지로 리스트로 표현했습니다.
        i=bin(i)
        b= '0'*(n+2-len(i)) + i[2:]
        list2.append(b)
    for i in range(n): # 빈 2차원리스트를 만들어주었습니다. 밑에서 채울예정입니다. 
        answer.append([])

    for i in range(n):  # 여기서는 list1과 list2를 겹쳐서 둘다 0인부분만 0으로 나타나게 만들었습니다.
        for j in range(n):
            if list1[i][j]=='0' and list2[i][j]=='0':
                answer[i].append(' ')
            else:
                answer[i].append('#')
    for i in answer:     # 이부분은 answer에 담겨잇는 리스트를 문자열로 변경시켜서 리스트로 나타낸 부분입니다. 
        for j in range(n):
            answer1= answer1+i[j]
        answer2.append(answer1)
        answer1 = ''             
    return answer2