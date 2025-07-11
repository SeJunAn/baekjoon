import sys

input = sys.stdin.readline

n = int(input().strip())

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    for j in [1, 2, 3]:
        if i > j:
            dp[i] += dp[i-j]

for _ in range(n):
    print(dp[int(input().strip())])