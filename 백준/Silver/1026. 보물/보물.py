import sys

input = sys.stdin.readline

n = int(input().strip())

arr1 = list(map(int, input().strip().split()))
arr2 = list(map(int, input().strip().split()))

sort_1 = sorted(arr1)
sort_2 = sorted(arr2, reverse=True)

result = 0

for i in range(n):
    result += sort_1[i] * sort_2[i]

print(result)