## DFS
N,M,V = map(int,input().split())
mlist = [] # 처음 연결값들 이중리스트로 묶은 리스트
stack = [] # stack 구조 list
newlist = [] # 최종 결과물
for_sort_list = [] # stack에 넣기전에 높은 숫자가 먼저 stack에 들어갈 수 있도록 처리하는 list
for i in range(M):
    new = list(map(int,input().split()))
    mlist.append(new)

stack.append(V)
while len(stack)>0:
    pop_value = stack.pop()
    if pop_value not in newlist:
        newlist.append(pop_value)    # 여기서 newlist에 값 넣음 
    a= len(mlist)   
    for i in range(a):     # 여기서는 stack에 넣을 데이터 처리하는중임 - mlist에 stack에서 pop된 데이터가 있는 것들을 가져와서 처리
        if pop_value in mlist[i]:
            mlist[i].remove(pop_value)
            for_sort_list.append(mlist[i].pop())
    
    for_sort_list.sort()   # pop_value랑 연결된 데이터들 순서대로 정렬한것 
    len_of_sort = len(for_sort_list)
    for i in range(len_of_sort):
        final_check = for_sort_list.pop()
        if final_check not in newlist:
            stack.append(final_check)
for i in newlist:
    print(i,end = ' ')