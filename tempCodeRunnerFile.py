def solution(triangle):
    answer = 0
    for i in len(triangle):
        for j in range(len(triangle[i])):
            if i==0:
                pass
            elif j == 0:
                triangle[i][j] += triangle[i-1][0]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]
            else :
                triangle[i][j] = max(triangle[i-1][j-1]+triangle[i][j],triangle[i-1][j]+triangle[i][j])
    a= triangle[-1]
    a.sort()
    answer = a[-1]
    return answer