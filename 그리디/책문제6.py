a = int(input())
l = list(map(int, input().split()))
l.sort()
number = 1
answer = 0
if l[0] != 1:
    answer = 1
else:
    for i in range(1,len(l)):
        if l[i] - l[i-1] > 1:
            answer = l[i-1] + 1
            break;
        else:
            l[i] = l[i-1] + l[i]
    if answer == 0:
        answer = l[-1] + 1
print(answer)