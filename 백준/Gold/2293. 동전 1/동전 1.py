import sys

input = sys.stdin.readline

n, k = map(int, input().strip().split())
dp = [0] * (k + 1)
dp[0] = 1

a = []
for _ in range(n):
    a.append(int(input().strip()))

for i in a:
    for j in range(i, k + 1):
        dp[j] += dp[j - i]

print(dp[k])
