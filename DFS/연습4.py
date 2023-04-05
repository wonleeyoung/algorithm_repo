from collections import deque



n,m = list(map(int,input().split()))

stage = []
for i in range(n):
    stage.append(list(map(int,input())))

queue = deque()

dx = [0,0,1,-1]
dy = [1,-1,0,0]

#position = [0,0]
destination = [n-1,m-1]
queue.append([0,0])
finish = 0
while queue:
    popped = queue.popleft()
    for i in range(4):
        if (0<=popped[0]+dx[i]<n) and (0<=popped[1]+dy[i]<m) and (stage[popped[0]+dx[i]][popped[1]+dy[i]]!=0):
            queue.append([popped[0]+dx[i],popped[1]+dy[i]])
            stage[popped[0]+dx[i]][popped[1]+dy[i]] = stage[popped[0]][popped[1]] + 1
            if [popped[0]+dx[i],popped[1]+dy[i]] == [n-1,m-1]:
                finish = 1
                break
    if finish == 1:
        break

print(stage[n-1][m-1])