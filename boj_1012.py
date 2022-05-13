# 백준 1012 유기농 배추

T = int(input())

whole_list =[]

for i in range(T):
    whole_list.append([])
    M,N,K = list(map(int,input().split()))
    for j in range(K):
        whole_list[i].append(list(map(int,input().split())))
        
        
for i in range(len(whole_list)):
    count=0
    while len(whole_list[i])>0:   # list1에 아무것도 없으면 끝남
        stack = [whole_list[i].pop()]
        while len(stack)>0:   # 지렁이 1마리가 차지하는 배추 공간구하는 것임
            x,y = stack.pop()
            if [x-1,y] in whole_list[i]:
                stack.append([x-1,y])
                whole_list[i].remove([x-1,y])
            if [x+1,y] in whole_list[i]:
                stack.append([x+1,y])
                whole_list[i].remove([x+1,y])
            if [x,y-1] in whole_list[i]:
                stack.append([x,y-1])
                whole_list[i].remove([x,y-1])
            if [x,y+1] in whole_list[i]:
                stack.append([x,y+1])
                whole_list[i].remove([x,y+1])
        count+=1
    print(count)

    