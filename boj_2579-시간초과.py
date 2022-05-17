# dfs 방식 -> 시간초과! 
import sys
n = int(sys.stdin.readline())
score_list = []
for i in range(n):
    a= int(sys.stdin.readline())
    score_list.append(a)
list1 = [[0,-1,0]]
result_list = []
while len(list1)>0:
    score,index,step = list1.pop()
    if index == n-1:
        result_list.append(score)
    if index + 1 <= n-1 and step < 2:
        new1 = score + score_list[index+1]
        list1.append([new1,index + 1,step+1])
    
    if index + 2 <= n-1 and step <=2:
        new2 = score + score_list[index +2]
        list1.append([new2,index + 2, 1])

result_list.sort()
print(result_list[-1])



