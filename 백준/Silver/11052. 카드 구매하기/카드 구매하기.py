import sys

input = sys.stdin.readline

n = int(input().strip())

dp = [0] * (n + 1)

a = [x for x in list(map(int, input().strip().split()))]

if n >= 1:
    dp[1] = a[0]

for i in range(2, n + 1):
    max = a[i-1]
    for j in range(1, i):
        if dp[j] + dp[i - j] > max:
            max = dp[j] + dp[i - j]
    dp[i] = max

print(dp[n])