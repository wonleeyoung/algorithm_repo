def solution(m, n, puddles):
    grid = [[1 for j in range(m)] for i in range(n)]
    for i,j in puddles:
        grid[j-1][i-1] = 0
        if j-1 == 0:
            for k in range(i,m):
                grid[0][k]=0
        if i-1 == 0:
            for k in range(j,n):
                grid[k][0]=0
    for i in range(1,n):
        for j in range(1,m):
            if grid[i][j] != 0:
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
    
            
    
    
    answer = grid[n-1][m-1] % 1000000007
    return answer