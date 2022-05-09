while 1:
    number = int(input()) 
    if number == 0: # 0이 들어오면 끝낸다.
        break
    a=str(number)  # Input값을 자리수마다 인덱스로 사용하기 위해 문자로 바꿔준다. 
    count = 0
    value = 0
    for i in range(len(a),0,-1):  
        index = 1
        for j in range(i,0,-1):
            index = index * j
        value += index*int(a[count])
        count+=1
    print(value)