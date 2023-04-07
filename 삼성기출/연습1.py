n = int(input())
t = []
p = []

for i in range(n):
    a,b = map(int, input().split())
    t.append(a)
    p.append(b)

dp = [0 for i in range(n)]
if t[0] == 1:
    dp[0] = p[0]
else:
    dp[t[0]-1] = p[0]
    
    
for i in range(1,n):
    if i+t[i]-1 < n:
        dp[i+t[i]-1]=max(dp[i-1] + p[i],dp[i+t[i]-1])
    dp[i] = max(dp[i],dp[i-1])

print(max(dp))
    

    