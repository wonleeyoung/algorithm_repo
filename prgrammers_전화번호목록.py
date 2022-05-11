def solution(phone_book):
    answer = True
    dict1 = {}
    for i in range(1,21):
        dict1[i] = []
    for i in phone_book:
        dict1[len(i)].append(i)
    
    return answer