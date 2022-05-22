def solution(nums):
    answer = 0
    a = set(nums)
    b = len(nums)/2
    if len(a)>b:
        answer = b
    else:
        answer = len(a)
    
    return answer