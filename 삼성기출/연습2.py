from collections import deque


def bfs(virus, area):
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    queue = deque()
    for i in virus:
        queue.append(i)
    while queue:
        a = queue.popleft()
        for j in range(4):
            mx = a[0] + dx[j]
            my = a[1] + dy[j]
            if (0<=mx<n) and (0<=my<m) and (area[mx][my] == 0):
                area[mx][my] = 2
                queue.append([mx,my])
    
def make_virus(virus,area,n,m):
    virus = []
    for i in range(n):
        for j in range(m):
            if area[i][j] == 2:
                virus.append([i,j])

def count(area,n,m):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if area[i][j] == 0:
                cnt+=1
    return cnt           



n,m = map(int, input().split())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

empty = []
virus = []
block = []
for i in range(n):
    for j in range(m):
        if area[i][j] == 1:
            block.append([i,j])
        elif area[i][j] == 0:
            empty.append([i,j])
        elif area[i][j] == 2:
            virus.append([i,j])

q = len(empty)

copy_area = [[0 for j in range(m)] for i in range(n)]
cnt = 0
for z in range(q-2):
    for w in range(z+1,q-1):
        for e in range(w+1,q):
            for i in range(n):
                for j in range(m):
                    copy_area[i][j] =area[i][j]
            make_virus(virus,copy_area,n,m)
            copy_area[empty[z][0]][empty[z][1]] = 1
            copy_area[empty[w][0]][empty[w][1]] = 1
            copy_area[empty[e][0]][empty[e][1]] = 1
            
            bfs(virus,copy_area)
            cnt = max(cnt, count(copy_area,n,m))

print(cnt)
            