def solution(lottos, win_nums):
    num = 0
    correct = 0
    for i in lottos:
        if i ==0:
           num+=1
        elif i in win_nums:
            
            correct+=1
            win_nums.remove(i)
    best = correct + num
    def score(a):
        if a == 6:
            return 1
        elif a == 5:
            return 2
        elif a == 4:
            return 3
        elif a == 3:
            return 4
        elif a == 2:
            return 5
        else:
            return 6
    answer = [score(best),score(correct)]
    
    return answer