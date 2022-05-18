
n = int(input())
score_list = []
for i in range(n):
    a= int(input())
    score_list.append(a)
if n == 1:
    print(score_list[0])
    quit()
elif n == 2:
    print(score_list[0]+score_list[1])
    quit()
result_list = [score_list[0],score_list[0]+score_list[1],max(score_list[0]+score_list[2],score_list[1]+score_list[2])]
for i in range(3,n):
    result_list.append(max(result_list[i-3] + score_list[i-1] + score_list[i] , result_list[i-2] + score_list[i]))
print(result_list[-1])