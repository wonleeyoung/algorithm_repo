def solution(new_id):
    cont = [chr(i) for i in range(97,123)]
    cont.append('-')
    cont.append('_')
    cont.append('.')
    for i in range(0,10):
        cont.append(str(i))
    list1 = []
    for i in new_id:
        if ord(i) >= 65 and 90>=ord(i):
            list1.append(chr(ord(i)+32))
        else:
            list1.append(i)
    removelist = []
    for i in list1:
        if not (i in cont or type(i) == int):
            removelist.append(i)
    for i in removelist:
        list1.remove(i)
    index = 0
    check = 0 
    while 1:
        if list1[index] == '.':
            check +=1
        else:
            check = 0
        if check == 1 and len(list1) - 1 > index:
            index+=1
            
        elif check > 1:
            list1.pop(index)
            if len(list1) == index:
                break
        elif len(list1)-1 > index:
            index += 1
            check = 0
        elif len(list1) - 1 == index:
            break
    if len(list1) != 0 and list1[0] == '.':
        list1.pop(0)
    if len(list1) != 0 and list1[-1] == '.':
        list1.pop()
    if list1 == []:
        list1.append('a')
    if len(list1)>=16:
        list1 = list1[:15]
    if list1[-1] == '.':
        list1.pop()
    while len(list1)<3:
        list1.append(list1[-1])
        
    answer = ''
    for i in list1:
        answer= answer+i
    return answer