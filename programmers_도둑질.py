def solution(money):
    answer = 0
    a=[0 for i in range(len(money))] # 0부터시작
    b=[0 for i in range(len(money))] # 1부터시작
    c=[0 for i in range(len(money))] # 2부터시작
    
    a[0]=money[0]
    a[2]=a[0]+money[2]
    for i in range(3,len(money)):
        a[i] = max(a[i-3]+money[i],a[i-2]+money[i])
        
    b[1]=money[1]
    for i in range(3,len(money)):
        b[i] = max(b[i-3]+money[i],b[i-2]+money[i])
        
        
    c[2]=money[2]

    for i in range(4,len(money)):
        c[i] = max(c[i-3]+money[i],c[i-2]+money[i])
    q=[a[-2],a[-3],a[-4],b[-1],b[-2],b[-3],c[-1],c[-2],c[-3]]
    q.sort()
    answer= q[-1]
    return answer