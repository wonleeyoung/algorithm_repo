from collections import deque
a = input()
l = []
for i in a:
    l.append(int(i))
deq = deque(l)
length = len(deq)
while length != 1 :
    i = deq.popleft()
    j = deq.popleft()
    if i + j > i * j:
        deq.appendleft(i+j)
    else:
        deq.appendleft(i * j)
    length -= 1
print(deq.popleft())

    