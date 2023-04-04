from collections import deque

def dfs(frame, visited, x, y):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    queue = deque()
    
    visited[x][y] = True
    queue.append([x,y])
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            if (x+dx[i] >= 0) and (y+dy[i]>=0) and (x+dx[i]<n) and (y+dy[i]<m) and (visited[x+dx[i]][y+dy[i]] == False) and (frame[x+dx[i]][y+dy[i]] == '0'):
                visited[x+dx[i]][y+dy[i]] = True
                queue.append([x+dx[i],y+dy[i]])
                
    

n,m = list(map(int, input().split()))
result = 0
frame = []

for i in range(n):
    dummy = list(input())
    frame.append(dummy)

visited = [[False for i in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if (frame[i][j] == '0') and (visited[i][j] == False):
            dfs(frame,visited,i,j)
            print("dfs몇번?")
            result += 1

print(visited)
print(result)