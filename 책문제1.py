n,m,k = list(map(int, input().split()))
l = list(map(int, input().split()))
l.sort()
a1 = l[-1]
a2 = l[-2]
count = m//(k+1)
count1 = m%(k+1)
sum = 0
sum += (a1 * k + a2) * count
sum += count1 * a1
print(sum)