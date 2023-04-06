n = int(input())
store = list(map(int, input().split()))

dp = [0 for i in range(n)]

dp[0] = store[0]
dp[1] = store[1]
dp[2] = store[0] + store[2]

for i in range(3,n):
    dp[i] = max(dp[i-3]+store[i],dp[i-2]+store[i])
print(max(dp))